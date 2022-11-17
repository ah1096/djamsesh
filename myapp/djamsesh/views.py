from django.shortcuts import render
from django.http.response import Http404
from rest_framework.views import APIView
from .models import Song, Artist
from .serializers import SongSerializer, ArtistSerializer
from rest_framework.response import Response
from rest_framework import status

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

#END SONG//////////////////////////////////////////////////////////////////
#START ARTIST//////////////////////////////////////////////////////////////

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
            'createsongmsg' : 'Artist created successfully',
            'data' : serializer.data, 
        }

        return response
