from rest_framework import serializers
from .models import Song, Artist, Genre, Album, Playlist

class SongSerializer(serializers.ModelSerializer):
    class Meta:
        model = Song
        fields = "__all__"

class ArtistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artist
        fields = "__all__"

class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = "__all__"

class AlbumSerializer(serializers.ModelSerializer):
    class Meta:
        model = Album
        fields = "__all__"

class PlaylistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Playlist
        fields = "__all__"

#combos///////////////

class Album_SongSerializer(serializers.ModelSerializer):
    class Meta:
        model = Album_Song
        fields = '__all__'

class Artist_SongSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artist_Song
        fields = '__all__'

class Playlist_SongSerializer(serializers.ModelSerializer):
    class Meta:
        model = Playlist_Song
        fields = '__all__'