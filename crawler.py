import re

import requests
from bs4 import BeautifulSoup


class EpisodeData:
    """
    하나의 에피소드에 대한 정보를 갖도록 함
    """

    def __init__(self, episode_id, url_thumbnail, title, rating, created_date):
        self.episode_id = episode_id
        self.url_thumbnail = url_thumbnail
        self.title = title
        self.rating = rating
        self.created_date = created_date

    def __str__(self):
        return f'("에피소드" : {self.episode_id : <2}, ' \
               f'"이미지 URL" : {self.url_thumbnail : <52}, ' \
               f'"제목" : {self.title}, ' \
               f'"별점" : {self.rating}, ' \
               f'"등록일" : {self.created_date})'


def get_episode_list(webtoon_id, page):
    """
    고유ID(URL에서 titleId값)에 해당하는 웹툰의
    특정 page에 있는 에피소드 목록을 리스트로 리턴
    """

    # http: // comic.naver.com / webtoon / list.nhn?titleId = 703835 & page = 1
    url = 'https://comic.naver.com/webtoon/list.nhn'
    params = {
        'titleId': webtoon_id,
        'page': page,
    }
    response = requests.get(url, params)
    soup = BeautifulSoup(response.text, 'lxml')

    # test 목적으로 crawler_detail.html 파일 만들어서 사용
    # f = open('crawler_detail.html', 'rt')
    # source = f.read()
    # f.close()
    # soup = BeautifulSoup(source, 'lxml')

    # inspect 에서 보이는 tbody가 사라져서 바로 tr로 검색
    tr_list = soup.select('table.viewList > tr')

    episode_list = []
    for tr in tr_list:
        episode_id = re.search(r".*'(\d+)", tr.select_one('td:nth-of-type(1) a').get('onclick')).group(1)
        url_thumbnail = tr.select_one('td:nth-of-type(1) a').get('href')
        title = tr.select_one('td:nth-of-type(2) a').get_text(strip=True)
        rating = tr.select_one('td:nth-of-type(3) div strong').get_text(strip=True)
        created_date = tr.select_one('td:nth-of-type(4)').get_text(strip=True)

        episode = EpisodeData(episode_id=episode_id,
                              url_thumbnail=url_thumbnail,
                              title=title,
                              rating=rating,
                              created_date=created_date)
        episode_list.append(episode)
    return episode_list


if __name__ == "__main__":
    result = get_episode_list('597447', '1')
    for item in result:
        print(item)
