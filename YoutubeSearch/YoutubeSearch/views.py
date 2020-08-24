from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination
from rest_framework import status
from .models import Video
import requests
from .serializer import VideoSerializer
import time
from collections import OrderedDict 

##################CONSTANTS#################################
API_KEYS=['AIzaSyAHaOX_L8nmKQ2OyIf-mnG9zBuQfWnLJpU','AIzaSyAHaOX_L8nmKQ2OyIf-mnG9zBuQfWnLJpU']
CURR_KEY=0
SEARCH='football'
FETCH_FREQ=10 #in seconds
############################################################

#Works in a separte thread so works asyncrounsly
def updateDB():
	global FETCH_FREQ
	async_fetch()
	time.sleep(FETCH_FREQ)

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
class VideoList(APIView,PageNumberPagination):
	def get(self,request):
		page = int(self.request.GET.get('page', 1))
		page_size = int(self.request.GET.get('page_size', 10))
		videos = Video.objects.all()[(page-1)*page_size:page*page_size]
		serializerData = VideoSerializer(videos,many=True)

		return Response(serializerData.data)