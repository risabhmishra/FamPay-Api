from rest_framework import serializers
from api.models import APIVideos


class APIVideosSerializer(serializers.ModelSerializer):
    class Meta:
        model = APIVideos
        fields = '__all__'
