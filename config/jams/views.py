from django.shortcuts import render
from django.http.response import Http404
from rest_framework.viewsets import ModelViewSet
from .models import Song, Artist, ArtistSong, Album, AlbumSong
from .serializers import SongSerializer, ArtistSerializer, ArtistSongSerializer, AlbumSerializer, AlbumSongSerializer
from rest_framework.response import Response
from rest_framework import status

class SongViewSet(ModelViewSet):
    queryset = Song.objects.all()
    serializer_class = SongSerializer

class ArtistViewSet(ModelViewSet):
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer

class ArtistSongViewSet(ModelViewSet):
    queryset = ArtistSong.objects.all()
    serializer_class = ArtistSongSerializer

class AlbumViewSet(ModelViewSet):
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer

class AlbumSongViewSet(ModelViewSet):
    queryset = AlbumSong.objects.all()
    serializer_class = AlbumSongSerializer   