from django.contrib import admin
from django.urls import path
from .views import VideoList
from .views import updateDB
import multiprocessing 

app_name= 'YoutubeSearch'

urlpatterns = [
    path('admin/', admin.site.urls),
	path('videos/',  VideoList.as_view()),
]

asyncUpdate= multiprocessing.Process(target=updateDB)
asyncUpdate.start()
