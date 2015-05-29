from django.db import models
from django_countries.fields import CountryField

class Organization(models.Model):
    org_name = models.CharField(max_length=200)
    org_city = models.CharField(max_length=100)
    org_country = CountryField()

# Create your models here.
