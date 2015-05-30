from django.db import models
from django.contrib.auth.models import User

class Break(models.Model):
    description = models.CharField(max_length=200)
    created_by = models.ForeignKey(User, editable=False)
    office = models.ForeignKey('offices.Office')

# Create your models here.
