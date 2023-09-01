from django.db import models


class Task(models.Model):
    name = models.CharField()
    content = models.CharField()
    is_closed = models.BooleanField()
