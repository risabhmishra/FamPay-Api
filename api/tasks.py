import logging

from api.models import APIVideos
from YoutubeSearchAPI.settings import DEVELOPER_KEY, YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION, QUERY_TERM

from celery.task.schedules import crontab
from celery.decorators import periodic_task
from googleapiclient.discovery import build

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)


# Periodic Task that runs every minute fetching videos from youtube data api and populating it in the APIVideos Table.
@periodic_task(
    run_every=(crontab(minute='*/1')),
    name="search_youtube",
    ignore_result=True)
def youtube_search():
    youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION,
                    developerKey=DEVELOPER_KEY, cache_discovery=False)

    # Call the search.list method to retrieve results matching the specified query term.
    search_response = youtube.search().list(
        q=QUERY_TERM,
        part='id,snippet',
        type='video',
        order='date',
        maxResults=10,
        publishedAfter='2020-07-25T11:37:41.228849Z',
    ).execute()

    for search_result in search_response.get('items', []):
        if search_result['id']['kind'] == 'youtube#video':
            try:
                snippet = search_result['snippet']
                video = APIVideos(video_id=search_result['id']['videoId'],
                                  published_at=snippet['publishedAt'],
                                  channel_id=snippet['channelId'],
                                  title=snippet['title'],
                                  description=snippet['description'],
                                  thumbnail=snippet['thumbnails']['medium']['url'])
                video.save()
            except Exception as exception:
                logger.exception(exception)
