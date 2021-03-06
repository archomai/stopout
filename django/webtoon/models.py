import re

import requests
from bs4 import BeautifulSoup
from django.db import models


class Webtoon(models.Model):
    webtoon_id = models.CharField(max_length=100)
    title = models.CharField(max_length=200)

    def __str__(self):
        return self.title

    def get_episode_list(self):

        url = 'https://comic.naver.com/webtoon/list.nhn'
        params = {
            'titleId': self.webtoon_id,
            'page': '1',
        }
        response = requests.get(url, params)
        soup = BeautifulSoup(response.text, 'lxml')
        tr_list = soup.find('table').find_all('tr', class_='')

        for tr in tr_list[1:]:
            episode_id = re.search(r".*'(\d+)", tr.select_one('td:nth-of-type(1) a').get('onclick')).group(1)
            # exurl_thumbnail = tr.select_one('td:nth-of-type(1) a').get('href')
            title = tr.select_one('td:nth-of-type(2) a').get_text(strip=True)
            rating = tr.select_one('td:nth-of-type(3) div strong').get_text(strip=True)
            created_date = tr.select_one('td:nth-of-type(4)').get_text(strip=True)

            if not self.episode_set.all().filter(episode_id=episode_id).exists():
                episode = self.episode_set.create(
                        episode_id=episode_id,
                        title=title,
                        rating=rating,
                        created_date=created_date
                    )


class Episode(models.Model):
    webtoon = models.ForeignKey(Webtoon, on_delete=models.CASCADE)
    episode_id = models.CharField(max_length=100)
    title = models.CharField(max_length=200)
    rating = models.CharField(max_length=100)
    created_date = models.CharField(max_length=100)

    def __str__(self):
        return '{} | {} | {} | {}'.format(
            self.episode_id,
            self.title,
            self.rating,
            self.created_date
        )