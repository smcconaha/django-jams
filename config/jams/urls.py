from django.urls import path, include
from .views import SongViewSet, ArtistViewSet, ArtistSongViewSet, AlbumViewSet, AlbumSongViewSet
from rest_framework import routers

router = routers.SimpleRouter()
router.register(r'songs', SongViewSet)
router.register(r'artist', ArtistViewSet)
router.register(r'artist-songs', ArtistSongViewSet)
router.register(r'album', AlbumViewSet)
router.register(r'album-songs', AlbumSongViewSet)
router.register(r'genre', AlbumViewSet)
router.register(r'genre-songs', AlbumSongViewSet)
router.register(r'playlist', AlbumViewSet)
router.register(r'playlist-songs', AlbumSongViewSet)

urlpatterns = [
    path('', include(router.urls)),
]