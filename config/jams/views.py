from django.shortcuts import render
from django.http.response import Http404
from rest_framework.viewsets import ModelViewSet
from .models import Song, Artist, ArtistSong
from .serializers import SongSerializer, ArtistSerializer
from rest_framework.response import Response
from rest_framework import status

class SongViewSet(ModelViewSet):
    queryset = Song.objects.all()
    serializer_class = SongSerializer

class ArtistViewSet(ModelViewSet):
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer
