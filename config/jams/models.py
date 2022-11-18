from django.db import models
from django.core.validators import MinValueValidator

class Artist(models.Model):
    name = models.CharField(max_length=50,null=False, blank=False, unique=True)
    bio = models.TextField(max_length=500, null=False, blank=False, unique=True)

    def __str__(self):
        return self.name

class Album(models.Model):
    name = models.CharField(max_length=30,null=False, blank=False, unique=True)

    def __str__(self):
        return self.name

class Genre(models.Model):
    name = models.CharField(max_length=20,null=False, blank=False, unique=True)

    def __str__(self):
        return self.name

class Playlist(models.Model):
    name = models.CharField(max_length=30,null=False, blank=False, unique=True)

    def __str__(self):
        return self.name

class Song(models.Model):
    title = models.CharField(max_length=255)
    duration = models.FloatField(null=False, default=.01, validators=[MinValueValidator(.01)])
    num_plays = models.BigIntegerField(default=0, validators=[MinValueValidator(0)])
    explicit = models.BooleanField()
    artist = models.ManyToManyField(Artist, through='ArtistSong', related_name="artist_list") #RelatedName allows us to query Artist from the Song model, usefeul for reverse lookup
    album = models.ManyToManyField(Album, through='AlbumSong', related_name="album_list")
    genre = models.ManyToManyField(Genre, through='GenreSong', related_name="genre_list")
    playlist = models.ManyToManyField(Playlist, through='PlaylistSong', related_name="playlist_list")
    
    def __str__(self):
        return self.title

class ArtistSong(models.Model):
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    song = models.ForeignKey(Song, on_delete=models.CASCADE)

    class Meta:
        unique_together = (
            ['artist', 'song']
        )

class AlbumSong(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    song = models.ForeignKey(Song, on_delete=models.CASCADE)    

    class Meta:
        unique_together = (
            ['album', 'song']
    )

class GenreSong(models.Model):
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)
    song = models.ForeignKey(Song, on_delete=models.CASCADE)    

    class Meta:
        unique_together = (
            ['genre', 'song']
    )
    
class PlaylistSong(models.Model):
    playlist = models.ForeignKey(Playlist, on_delete=models.CASCADE)
    song = models.ForeignKey(Song, on_delete=models.CASCADE)    

    class Meta:
        unique_together = (
            ['playlist', 'song']
    )
