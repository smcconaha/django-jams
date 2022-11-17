from rest_framework import serializers
from .models import *
from pprint import pprint

class ArtistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artist
        fields = ('name',)

class SongSerializer(serializers.ModelSerializer):
    artists = ArtistSerializer(many=True)
    class Meta:
        model = Song
        fields = ('artists', 'title', 'duration', 'num_plays', 'explicit',)

    def create(self, validated_data):
        artist = validated_data.pop('artist')
        artist_instance = Artist.objects.get(name=artist['name'])
        song = Song.objects.create(**validated_data, category=artist_instance)
        return song

class ArtistSongSerializer(serializers.ModelSerializer):
    class Meta:
        model = ArtistSong
        fields = "__all__"
