from django.urls import path, include
from .views import SongViewSet, ArtistViewSet
from rest_framework import routers

router = routers.SimpleRouter()
router.register(r'songs', SongViewSet)
router.register(r'artists', ArtistViewSet)

urlpatterns = [
    path('', include(router.urls)),
]