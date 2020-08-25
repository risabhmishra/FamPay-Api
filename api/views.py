from rest_framework import generics
from rest_framework import filters

from api.serializers import APIVideosSerializer
from api.models import APIVideos


class APIVideosList(generics.ListCreateAPIView):
    """
    List all stored video data in a paginated response sorted in descending order of published datetime.
    Query search text in the title and description field of APIVideos Model class.
    """

    search_fields = ['title', 'description']
    filter_backends = (filters.SearchFilter,)
    queryset = APIVideos.objects.all().order_by('-published_at')
    serializer_class = APIVideosSerializer
