from rest_framework import viewsets
from .serializers import AlbumSerializer, PhotoSerializer, UserSerializer
from django.contrib.auth.models import User
from album.models import Album, Photo


class AlbumViewSet(viewsets.ModelViewSet):
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer


class PhotoViewSet(viewsets.ModelViewSet):
	queryset = Photo.objects.all()
	serializer_class = PhotoSerializer


class UserViewSet(viewsets.ReadOnlyModelViewSet):
	queryset = User.objects.all()
	serializer_class = UserSerializer