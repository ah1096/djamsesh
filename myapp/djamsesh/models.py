from django.db import models
#from datetime import date????????????


class Song(models.Model):
    #id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=100)
    mainartist = models.ForeignKey('Artist', default=None, on_delete=models.PROTECT)
    featuredartists = models.ForeignKey('Artist', default=None, on_delete=models.PROTECT)
    #album_id = models.ForeignKey('Album', default=None, on_delete=models.PROTECT)
    explicit = models.BooleanField(default=False)
    #genre_id = models.ForeignKey('Genre', default=None, on_delete=models.PROTECT)
    #times_played = models.IntegerField(default=0)

    #playlists = models.ManyToManyField(Playlist)

    #release_date = models.DateField()????????????????

class Artist(models.Model):
    name = models.CharField(max_length=100)
    bio = models.CharField(max_length=200)
    imageURL = models.CharField(max_length=250)
    #genre_id = models.ForeignKey('Genre', default=None, on_delete=models.PROTECT)
    
    

class Album(models.Model):
    coverURL = models.CharField(max_length=250)
    title = models.CharField(max_length=100)
    song_id = models.ForeignKey('Song', default=None, on_delete=models.PROTECT)
    artist_id = models.ForeignKey('Artist', default=None, on_delete=models.PROTECT)
    genre_id = models.ForeignKey('Genre', default=None, on_delete=models.PROTECT)

    #release_date = models.DateField()????????

class Genre(models.Model):
    #id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    

class Playlist(models.Model):
    #id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=100)
    song_id = models.ForeignKey('Song', default=None, on_delete=models.PROTECT)







    
