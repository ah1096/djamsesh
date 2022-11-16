from rest_framework import serializers
from .models import Song, Artist, Album, Genre, Playlist

class SongSerializer(serializers.ModelSerializer):
    class Meta:
        model = Song
        fields = "__all__"