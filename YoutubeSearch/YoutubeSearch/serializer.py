from rest_framework import serializers
from .models import Video

class VideoSerializer(serializers.ModelSerializer):

	title = serializers.CharField()
	description = serializers.CharField()
	publishDate = serializers.DateTimeField()
	thumbnailURL = serializers.CharField()
	videoURL = serializers.CharField()

	def create(self, validated_data):
		return CustomUser.objects.create(**validated_data)

	class Meta:
		model = Video
		fields = ('title','description','publishDate','thumbnailURL','videoURL')