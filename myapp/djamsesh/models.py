from django.db import models


class Song(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=100)
    explicit = models.BooleanField(default=False)
    times_played = models.IntegerField(default=0)
    #artist_id = 
    #genre_id =
    #album_id = 
    #release_date = models.DateTimeField(default=timezone.now)

class Artist(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    bio = models.CharField(max_length=200)
    imageURL = models.CharField(max_length=250)
    #genre_id =
    #release_date = models.DateTimeField(default=timezone.now)
    

class Album(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=100)
    coverURL = models.CharField(max_length=250)
    #artist_id = 
    #genre_id = 
    #song_id = 
    #release_date = models.DateTimeField(default=timezone.now)

class Genre(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)

class Playlist(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=100)
    #song_id = 







    
