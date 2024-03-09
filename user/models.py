from django.contrib.auth.models import User
from django.db import models

from django.db import models
from django import forms


class NatalChartAnalysis(models.Model):
    Name= models.CharField(max_length=100,default='guest')
    birth_date = models.DateField()
    birth_time = models.TimeField()
    birth_place = models.CharField(max_length=100)
    def __str__(self):
        return self.Name

class zodaic(models.Model):
    name = models.CharField(max_length=100)
    birth_date = models.DateField()

    def __str__(self):
        return self.name

class dailyhoroscopes(models.Model):
    name= models.CharField(max_length=100)
    birth_day = models.IntegerField()  # Day of birth
    birth_month = models.IntegerField()  # Month of birth
    birth_year = models.IntegerField()  # Year of birth

    def __str__(self):
         return self.name


class weeklyhoroscopes(models.Model):
    name= models.CharField(max_length=100)
    birth_day = models.IntegerField()  # Day of birth
    birth_month = models.IntegerField()  # Month of birth
    birth_year = models.IntegerField()  # Year of birth

    def __str__(self):
         return self.name


class monthlyhoroscopes(models.Model):
    name= models.CharField(max_length=100)
    birth_day = models.IntegerField()  # Day of birth
    birth_month = models.IntegerField()  # Month of birth
    birth_year = models.IntegerField()  # Year of birth

    def __str__(self):
         return self.name


class yearlyhoroscopes(models.Model):
    name= models.CharField(max_length=100)
    birth_day = models.IntegerField()  # Day of birth
    birth_month = models.IntegerField()  # Month of birth
    birth_year = models.IntegerField()  # Year of birth

    def __str__(self):
         return self.name