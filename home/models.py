from turtle import mode
from django.db import models


class PartnersModel(models.Model):
    image = models.ImageField(blank=True,null=True)

