from turtle import mode
from django.db import models


class HomeModel(models.Model):
    title = models.CharField(max_length=300)
    sub_title = models.CharField(max_length=300)
    info = models.TextField()
    image = models.ImageField(blank=True)


