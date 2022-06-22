from turtle import title
from django.db import models

# Create your models here.

class Project(models.Model):
    title = models.CharField(max_length=70)
    repo = models.CharField(max_length=200)
    live = models.CharField(max_length=200)
    description = models.TextField()

    def __str__(self):
        return title