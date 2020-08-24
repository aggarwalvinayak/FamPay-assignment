from django.contrib import admin
from .models import Video
from django.contrib.admin import ModelAdmin

class VideoAdmin(ModelAdmin):
    model = Video
    list_display = ('title','description','publishDate','thumbnailURL','videoURL')
    list_filter = ('title','description','publishDate','thumbnailURL','videoURL')
    ordering = ['-publishDate']

admin.site.register(Video,VideoAdmin)
