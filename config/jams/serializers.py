from rest_framework import serializers
from .models import Song, Artist, ArtistSong
from pprint import pprint

class ArtistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artist
        fields = "__all__"

class SongSerializer(serializers.ModelSerializer):
    artist = ArtistSerializer()
    class Meta:
        model = Song
        fields = "__all__"

    def create(self, validated_data):
        artist = validated_data.pop('artist')
        cat_instance = Artist.objects.get(name=artist['name'])
        todo = Todo.objects.create(**validated_data, category=cat_instance)
        return Song