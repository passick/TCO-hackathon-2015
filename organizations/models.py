from django.db import models
from django_countries.fields import CountryField

class Organization(models.Model):
    name = models.CharField(max_length=200)
    city = models.CharField(max_length=100)
    country = CountryField()

class Office(models.Model):
    organization = models.ForeignKey(Organization)
    name = models.CharField(max_length=100)

class Break(models.Model):
    office = models.ForeignKey(Office)
    description = models.CharField(max_length=300)
    duration = models.DurationField()

# Create your models here.
