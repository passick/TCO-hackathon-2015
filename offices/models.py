from django.db import models

class Office(models.Model):
    name = models.CharField(max_length=100)
    organization = models.ForeignKey('organizations.Organization')

# Create your models here.
