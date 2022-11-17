from rest_framework import serializers
from .models import *
from pprint import pprint

class ArtistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artist
        fields = ('name',)

class AlbumSerializer(serializers.ModelSerializer):
    class Meta:
        model = Album
        fields = ('name',)

class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ('name',)

class PlaylistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Playlist
        fields = ('name',)

class SongSerializer(serializers.ModelSerializer):
    artist = ArtistSerializer(many=True)
    album = AlbumSerializer(many=True)
    genre = GenreSerializer(many=True)
    playlist = PlaylistSerializer(many=True)
    class Meta:
        model = Song
        fields = ('artist', 'title', 'duration', 'num_plays', 'genre', 'explicit', 'album','playlist',)

    def create(self, validated_data):
        artist = validated_data.pop('artist')
        artist_instance = Artist.objects.get(name=artist['name'])
        song = Song.objects.create(**validated_data, category=artist_instance)
        return song

class ArtistSongSerializer(serializers.ModelSerializer):
    class Meta:
        model = ArtistSong
        fields = "__all__"

class AlbumSongSerializer(serializers.ModelSerializer):
    class Meta:
        model = AlbumSong
        fields = "__all__"

class GenreSongSerializer(serializers.ModelSerializer):
    class Meta:
        model = GenreSong
        fields = "__all__"

class PlaylistSongSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlaylistSong
        fields = "__all__"