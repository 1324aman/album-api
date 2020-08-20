from album.models import Album, Photo
from django.contrib.auth.models import User
from rest_framework import serializers


class PhotoSerializer(serializers.HyperlinkedModelSerializer):
	#owner = serializers.ReadOnlyField(source='owner.username')
	#album = serializers.ReadOnlyField(source='album.title')
	class Meta:
		model = Photo
		fields =  ['id', 'image_url', 'owner', 'album']


class PhotoSerializerForNesting(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Photo
		fields = ['image_url', 'owner']



class AlbumSerializer(serializers.HyperlinkedModelSerializer):
	photos = PhotoSerializerForNesting(many=True, read_only=True, source='photo_set')
	class Meta:
		model = Album
		fields = ['title', 'photos']


class UserSerializer(serializers.HyperlinkedModelSerializer):
	class Meta: 
		model = User
		fields = ['username']
