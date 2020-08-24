from django.db import models
from django.conf import settings
from django.db import models

class Videos(models.Model):
	title = models.CharField(max_length=100)
	description = models.CharField(max_length=1000)
	publishDate = models.DateTimeField()
	thumbnailURL = models.CharField(max_length=500)
	videoURL = models.CharField(max_length=500)