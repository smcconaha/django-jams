from django.urls import path, include
from .views import SongViewSet, ArtistViewSet, ArtistSongViewSet
from rest_framework import routers

router = routers.SimpleRouter()
router.register(r'songs', SongViewSet)
router.register(r'artists', ArtistViewSet)
router.register(r'artist-songs', ArtistSongViewSet)

urlpatterns = [
    path('', include(router.urls)),
]