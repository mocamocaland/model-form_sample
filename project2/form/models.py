from django.db import models
from django.utils import timezone


class Category(models.Model):
    name = models.CharField('タイトル', max_length=30)

    def __str__(self):
        return self.name


class Day(models.Model):
    title = models.CharField('タイトル', max_length=200)
    text = models.TextField('本文')
    date = models.DateTimeField('日付', default=timezone.now)
    category = models.ForeignKey(Category, related_name='カテゴリ', on_delete=models.PROTECT)

    def __str__(self):
        return self.title
