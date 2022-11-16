from rest_framework import serializers
from .models import Song
from pprint import pprint

class SongSerializer(serializers.ModelSerializer):
    class Meta:
        model = Song
        fields = "__all__"