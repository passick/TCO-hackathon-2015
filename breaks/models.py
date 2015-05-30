from django.db import models
from django.contrib.auth.models import User

from datetime import timedelta

class Break(models.Model):
    description = models.CharField(max_length=200)
    created_by = models.ForeignKey(User, editable=False)
    office = models.ForeignKey('offices.Office')
    duration = models.DurationField(default=timedelta())
    start_time = models.DateTimeField()

# Create your models here.
