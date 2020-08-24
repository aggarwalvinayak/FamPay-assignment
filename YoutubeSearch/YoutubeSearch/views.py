from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Videos
import requests

def async_fetch():
	API_KEY='AIzaSyAHaOX_L8nmKQ2OyIf-mnG9zBuQfWnLJpU'
	SEARCH='cricket+football'
	URL = 'https://www.googleapis.com/youtube/v3/search?key='+API_KEY+'&type=video&order=date&part=snippet&q='+SEARCH
	response = requests.get(URL).json()

	for video in response.items:
		try:
			Videos.objects.get_or_create(
				title = video.snippet.title,
				description = video.snippet.description,
				publishDate = video.snippet.publishedAt,
				thumbnailURL = video.snippet.thumbnails.default.url,
				videoURL="https://www.youtube.com/watch?v="+video.id.videoId)
		except:
			print("Error in fetch")
			break


