from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Person(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nick_name = models.CharField(max_length=100)

    def __str__(self):
        return self.nick_name


class Stock(models.Model):
    ticker = models.CharField(max_length=10)  
    volume = models.FloatField()
    low = models.FloatField()
    high = models.FloatField()

    def __str__(self):
        return self.ticker
    
