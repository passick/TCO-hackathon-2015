from django.db import models
from django_countries.fields import CountryField

class Organization(models.Model):
    name = models.CharField(max_length=200)
    country = CountryField()
    city = models.CharField(max_length=100)

# Create your models here.
