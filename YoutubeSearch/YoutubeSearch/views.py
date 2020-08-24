from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Video
import requests
from .serializer import VideoSerializer
import time

##################CONSTANTS#################################
API_KEYS=['AIzaSyAHaOX_L8nmKQ2OyIf-mnG9zBuQfWnLJpU','AIzaSyAHaOX_L8nmKQ2OyIf-mnG9zBuQfWnLJpU']
CURR_KEY=0
SEARCH='football'
############################################################

#Works in a separte thread so works asyncrounsly
def updateDB():
	async_fetch()
	time.sleep(10)

#Fetches from the Youtube API & Updates in the local database
def async_fetch():
	global	API_KEYS,SEARCH,CURR_KEY
	URL = 'https://www.googleapis.com/youtube/v3/search?key='+API_KEYS[CURR_KEY]+'&type=video&order=date&part=snippet&maxResults=20&q='+SEARCH
	response = requests.get(URL).json()

	try:
		for video in response['items']:
			Video.objects.get_or_create(
				title = video['snippet']['title'],
				description = video['snippet']['description'],
				publishDate = video['snippet']['publishedAt'],
				thumbnailURL = video['snippet']['thumbnails']['high']['url'],
				videoURL="https://www.youtube.com/watch?v="+video['id']['videoId'])
	except:
		CURR_KEY=(CURR_KEY+1)%len(API_KEYS)
		print("Error in fetch")
		

#GET API for the video Database
class VideoList(APIView):
	def get(self,request):
		videos = Video.objects.all()
		serializer = VideoSerializer(videos,many=True)
		return Response(serializer.data)