from __future__ import unicode_literals

from django.db import models

class Report(models.Model):
    name = models.CharField(max_length=15)
    interval = models.PositiveIntegerField()
