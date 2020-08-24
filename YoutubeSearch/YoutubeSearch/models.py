from django.db import models
from django.conf import settings
from django.db import models

class Videos(models.Model):
	title = models.charField(max_length=100)
	description = models.charField(max_length=1000)
	publishDate = models.DateTimeField()
	thumbnailURL = models.charField(max_length=500)
	videoURL = models.charField(max_length=500)