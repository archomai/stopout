from django.db import models


class Webtoon(models.Model):
    webtoon_id = models.CharField(max_length=100)
    title = models.CharField(max_length=200)

    def __str__(self):
        return self.title


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