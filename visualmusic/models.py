from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Song(models.Model):
	song_title = models.CharField(max_length=200)
	song_artist = models.CharField(max_length=200)

