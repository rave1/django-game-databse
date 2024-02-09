from django.db import models

# Create your models here.


class Game(models.Model):
    name = models.CharField(max_length=256)
    image = models.URLField()
    platform = models.CharField(max_length=64)
    users = models.ManyToManyField('accounts.User')
