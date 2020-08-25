from django.db import models


class APIVideos(models.Model):
    video_id = models.CharField(max_length=55, primary_key=True)
    channel_id = models.CharField(max_length=55, blank=True, null=True)
    title = models.CharField(max_length=255, blank=True, null=True)
    description = models.CharField(max_length=255, blank=True, null=True)
    published_at = models.DateTimeField(blank=True, null=True)
    thumbnail = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.title
