from django.db import models
from datetime import datetime as dt

YEAR_NOW = int(dt.now().strftime('%Y'))


class Category(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name


class Genre(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name


class Title(models.Model):
    name = models.CharField(max_length=200)
    year = models.IntegerField(default=YEAR_NOW)
    description = models.CharField(max_length=200)
    genre = models.ForeignKey(
        Genre, on_delete=models.SET_NULL,
        related_name='titles', blank=True, null=True
    )
    category = models.ForeignKey(
        Category, on_delete=models.SET_NULL,
        related_name='titles', blank=True, null=True
    )
