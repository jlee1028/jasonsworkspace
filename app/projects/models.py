from django.db import models

# Create your models here.

# Class == table
# attributes == columns


class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    technology = models.CharField(max_length=20)
    image = models.CharField(max_length=100)
    interactive = models.BooleanField()
    html_path = models.CharField(max_length=100, default="")
