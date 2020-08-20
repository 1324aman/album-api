from django.db import models
from django.contrib.auth.models import User


class Album(models.Model):
	title = models.CharField(max_length=100)


class Photo(models.Model):
	owner = models.ForeignKey(User, on_delete=models.CASCADE)
	album = models.ForeignKey(Album, on_delete=models.CASCADE)
	image_url = models.URLField(max_length = 200)
