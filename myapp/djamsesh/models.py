from django.db import models

class Song(models.Model):
    title = models.CharField(max_length=100)
    explicit = models.BooleanField(default=False)

class Artist(models.Model):
    name = models.CharField(max_length=100)
    bio = models.CharField(max_length=200)
    imageURL = models.CharField(max_length=250) 

class Album(models.Model):
    coverURL = models.CharField(max_length=250)
    title = models.CharField(max_length=100)

class Genre(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(default=None, max_length=200)

class Playlist(models.Model):
    title = models.CharField(max_length=100)








    
