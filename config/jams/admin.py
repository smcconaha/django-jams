from django.contrib import admin

from .models import *

admin.site.register(Artist)
admin.site.register(Album)
admin.site.register(Genre)
admin.site.register(Playlist)
admin.site.register(Song)
admin.site.register(ArtistSong)
admin.site.register(AlbumSong)
admin.site.register(GenreSong)
admin.site.register(PlaylistSong)