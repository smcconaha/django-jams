from django.db import models
from django.core.validators import MinValueValidator

class Artist(models.Model):
    name = models.CharField(max_length=50,null=False, blank=False, unique=True)
    bio = models.TextField(max_length=500, null=False, blank=False, unique=True)

class Song(models.Model):
    title = models.CharField(max_length=255)
    duration = models.FloatField(null=False, default=.01, validators=[MinValueValidator(.01)])
    num_plays = models.BigIntegerField(default=0, validators=[MinValueValidator(0)])
    explicit = models.BooleanField()
    artists = models.ManyToManyField(Artist, through='ArtistSong', related_name="artist_list") #RN allows us to query Artist from the Song model, usefeul for reverse lookup

class ArtistSong(models.Model):
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    song = models.ForeignKey(Song, on_delete=models.CASCADE)

    class Meta:
        unique_together = (
            ['artist', 'song']
        )

    