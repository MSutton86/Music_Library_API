from django.db import models

# Create your models here.

class Music(models.Model):
    title = models.CharField(max_length=85)
    artist = models.CharField(max_length=85)
    album = models.CharField(max_length=165)
    release_date = models.DateField(null=True)
    genre = models.CharField(max_length=85)
    