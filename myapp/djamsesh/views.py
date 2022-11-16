from django.shortcuts import render
from django.http.response import Http404
from rest_framework.views import APIView
from .models import Song, Artist, Album, Genre, Playlist
from .serializers import SongSerializer
from rest_framework.response import Response

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
            data = Todo.objects.all()
            serializer = SongSerializer(data, many=True)

            return Response(serializer.data)  

#CREATE//////////////////////////////////////////////JSON > Python
    def post(self, request, format=None):
        data = request.data
        serializer = SongSerializer(data=data)

        #validate data
        serializer.is_valid(raised_exception=True)
        #save the Song to the database
        serializer.save()
        #tell frontend about save result (success or not)
        response = Response()

        response.data = {
            'createsongmsg' : 'Song created successfully',
            'data' : serializer.data, 
        }

        return response
        
