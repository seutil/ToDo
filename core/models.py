from django.db import models


class Task(models.Model):
    name = models.CharField(max_length=255)
    content = models.CharField(max_length=255)
    is_closed = models.BooleanField()
