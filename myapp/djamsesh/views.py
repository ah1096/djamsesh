from django.shortcuts import render
from django.http.response import Http404
from rest_framework.views import APIView
from .models import Song, Artist, Genre, Album, Playlist
from .serializers import SongSerializer, ArtistSerializer, GenreSerializer, AlbumSerializer, PlaylistSerializer
from rest_framework.response import Response
from rest_framework import status







class Album_SongList(generics.ListCreateAPIView):
    queryset = Album_Song.objects.all()
    serializer_class = Album_SongSerializer

class Album_SongDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Album_Song.objects.all()
    serializer_class = Album_SongSerializer

class Artist_SongList(generics.ListCreateAPIView):
    queryset = Artist_Song.objects.all()
    serializer_class = Artist_SongSerializer

class Artist_SongDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Artist_Song.objects.all()
    serializer_class = Artist_SongSerializer


class GenreList(generics.ListCreateAPIView):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer

class GenreDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer


class PlaylistList(generics.ListCreateAPIView):
    queryset = Playlist.objects.all()
    serializer_class = PlaylistSerializer

class PlaylistDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Playlist.objects.all()
    serializer_class = PlaylistSerializer

class AlbumList(generics.ListCreateAPIView):
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer

class AlbumDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer




#aezsdrftghj/////////////////////////////////////////////////////////////////////////
#ertyhjk/////////////////////////////////////////////////////////////////////////////

class SongAPIView(APIView):
    def get_object(self, pk):
        try:
            return Song.objects.get(pk=pk)
        except Song.DoesNotExist:
            raise Http404

#READ////////////////////////////////////////////////Python > JSON
    def get(self, request, pk=None, format=None):
        if pk:
            data = self.get_object(pk)
            serializer = SongSerializer(data)
        else:
            data = Song.objects.all()
            serializer = SongSerializer(data, many=True)

        return Response(serializer.data)  

#CREATE//////////////////////////////////////////////JSON > Python
    def post(self, request, format=None):
        print("You sent a post request")

        data = request.data
        serializer = SongSerializer(data=data)

        #validate data
        serializer.is_valid(raise_exception=True)
        #save the Song to the database
        serializer.save()
        #tell frontend about save result (success or not)
        response = Response()

        response.data = {
            'createsongmsg' : 'Song created successfully',
            'data' : serializer.data, 
        }

        return response

#UPDATE/////////////////////////////////////////////
    def put(self, request, pk=None, format=None):
        song_to_update = Song.objects.get(pk=pk)
        data = request.data
        serializer = SongSerializer(instance = song_to_update, data=data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        response = Response()

        response.data = {
            'updatesongmsg' : 'song updated successfully',
            'data' : serializer.data
        }
        return response

#DELETE/////////////////////////////////////////////
    def delete(self, request, pk, format=None):
        song_to_delete = self.get_object(pk)
        song_to_delete.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

#qqqq/////////////////////////////////////////////
#ARTIST/////////////////////////////////////////////

class ArtistAPIView(APIView):
    def get_object(self, pk):
        try:
            return Artist.objects.get(pk=pk)
        except Artist.DoesNotExist:
            raise Http404

#READ////////////////////////////////////////////////Python > JSON
    def get(self, request, pk=None, format=None):
        if pk:
            data = self.get_object(pk)
            serializer = ArtistSerializer(data)
        else:
            data = Artist.objects.all()
            serializer = ArtistSerializer(data, many=True)

        return Response(serializer.data)  

#CREATE//////////////////////////////////////////////JSON > Python
    def post(self, request, format=None):
        print("You sent a post request")

        data = request.data
        serializer = ArtistSerializer(data=data)

        #validate data
        serializer.is_valid(raise_exception=True)
        #save the Song to the database
        serializer.save()
        #tell frontend about save result (success or not)
        response = Response()

        response.data = {
            'createartistmsg' : 'Artist created successfully',
            'data' : serializer.data, 
        }

        return response

#UPDATE/////////////////////////////////////////////
    def put(self, request, pk=None, format=None):
        artist_to_update = Artist.objects.get(pk=pk)
        data = request.data
        serializer = ArtistSerializer(instance = artist_to_update, data=data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        response = Response()

        response.data = {
            'updatesongmsg' : 'song updated successfully',
            'data' : serializer.data
        }
        return response

#DELETE/////////////////////////////////////////////
    def delete(self, request, pk, format=None):
        artist_to_delete = self.get_object(pk)
        artist_to_delete.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


#qqqq/////////////////////////////////////////////
#GENRE/////////////////////////////////////////////

class GenreAPIView(APIView):
    def get_object(self, pk):
        try:
            return Genre.objects.get(pk=pk)
        except Genre.DoesNotExist:
            raise Http404

#READ////////////////////////////////////////////////Python > JSON
    def get(self, request, pk=None, format=None):
        if pk:
            data = self.get_object(pk)
            serializer = GenreSerializer(data)
        else:
            data = Genre.objects.all()
            serializer = GenreSerializer(data, many=True)

        return Response(serializer.data)  

#CREATE//////////////////////////////////////////////JSON > Python
    def post(self, request, format=None):
        print("You sent a post request")

        data = request.data
        serializer = GenreSerializer(data=data)

        #validate data
        serializer.is_valid(raise_exception=True)
        #save the Song to the database
        serializer.save()
        #tell frontend about save result (success or not)
        response = Response()

        response.data = {
            'creategenremsg' : 'Genre created successfully',
            'data' : serializer.data, 
        }

        return response

#UPDATE/////////////////////////////////////////////
    def put(self, request, pk=None, format=None):
        artist_to_update = Genre.objects.get(pk=pk)
        data = request.data
        serializer = GenreSerializer(instance = genre_to_update, data=data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        response = Response()

        response.data = {
            'updategenremsg' : 'genre updated successfully',
            'data' : serializer.data
        }
        return response

#DELETE/////////////////////////////////////////////
    def delete(self, request, pk, format=None):
        genre_to_delete = self.get_object(pk)
        genre_to_delete.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

#qqqq/////////////////////////////////////////////
#ALBUM/////////////////////////////////////////////

class AlbumAPIView(APIView):
    def get_object(self, pk):
        try:
            return Album.objects.get(pk=pk)
        except Album.DoesNotExist:
            raise Http404

#READ////////////////////////////////////////////////Python > JSON
    def get(self, request, pk=None, format=None):
        if pk:
            data = self.get_object(pk)
            serializer = AlbumSerializer(data)
        else:
            data = Album.objects.all()
            serializer = AlbumSerializer(data, many=True)

        return Response(serializer.data)  

#CREATE//////////////////////////////////////////////JSON > Python
    def post(self, request, format=None):
        print("You sent a post request")

        data = request.data
        serializer = AlbumSerializer(data=data)

        #validate data
        serializer.is_valid(raise_exception=True)
        #save the Song to the database
        serializer.save()
        #tell frontend about save result (success or not)
        response = Response()

        response.data = {
            'createalbummsg' : 'Album created successfully',
            'data' : serializer.data, 
        }

        return response

#UPDATE/////////////////////////////////////////////
    def put(self, request, pk=None, format=None):
        album_to_update = Album.objects.get(pk=pk)
        data = request.data
        serializer = AlbumSerializer(instance = album_to_update, data=data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        response = Response()

        response.data = {
            'updatealbummsg' : 'album updated successfully',
            'data' : serializer.data
        }
        return response

#DELETE/////////////////////////////////////////////
    def delete(self, request, pk, format=None):
        album_to_delete = self.get_object(pk)
        album_to_delete.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


#qqqq/////////////////////////////////////////////
#PLAYLIST/////////////////////////////////////////////

class PlaylistAPIView(APIView):
    def get_object(self, pk):
        try:
            return Playlist.objects.get(pk=pk)
        except Playlist.DoesNotExist:
            raise Http404

#READ////////////////////////////////////////////////Python > JSON
    def get(self, request, pk=None, format=None):
        if pk:
            data = self.get_object(pk)
            serializer = PlaylistSerializer(data)
        else:
            data = Playlist.objects.all()
            serializer = PlaylistSerializer(data, many=True)

        return Response(serializer.data)  

#CREATE//////////////////////////////////////////////JSON > Python
    def post(self, request, format=None):
        print("You sent a post request")

        data = request.data
        serializer = PlaylistSerializer(data=data)

        #validate data
        serializer.is_valid(raise_exception=True)
        #save the Song to the database
        serializer.save()
        #tell frontend about save result (success or not)
        response = Response()

        response.data = {
            'createplaylistmsg' : 'Playlist created successfully',
            'data' : serializer.data, 
        }

        return response

#UPDATE/////////////////////////////////////////////
    def put(self, request, pk=None, format=None):
        playlist_to_update = Playlist.objects.get(pk=pk)
        data = request.data
        serializer = PlaylistSerializer(instance = playlist_to_update, data=data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        response = Response()

        response.data = {
            'updateplaylistmsg' : 'playlist updated successfully',
            'data' : serializer.data
        }
        return response

#DELETE/////////////////////////////////////////////
    def delete(self, request, pk, format=None):
        album_to_delete = self.get_object(pk)
        album_to_delete.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

#rdcfgvhbjn///////////////////////////////////////////
#rdcfgvhbjn///////////////////////////////////////////


