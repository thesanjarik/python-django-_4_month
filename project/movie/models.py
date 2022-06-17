from django.db import models

# Create your models here.

class Movie(models.Model):
    name = models.CharField(max_length=100)
    title = models.CharField(max_length=200)
    description = models.TextField(max_length=2000, blank=True)
    text = models.TextField(max_length=1000)

    def __str__(self):
        return self.title




# Вывести на страницу список фильмов - 127.0.0.1:8000/movies/
# Вывести на страницу один фильм -  127.0.0.1:8000/movies/<int:id>/


# Вывести на страницу список режиссеров - 127.0.0.1:8000/directors/
# Вывести на страницу одного режиссера -  127.0.0.1:8000/directors/<int:id>/


# Вывести на страницу список отзывов - 127.0.0.1:8000/reviews/
# Вывести на страницу один отзыв -  127.0.0.1:8000/reviews/<int:id>/
