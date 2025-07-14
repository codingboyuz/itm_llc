from turtle import mode
from django.db import models


class PartnersModel(models.Model):
    image = models.ImageField(upload_to="media/partners/" ,blank=True,null=True)

