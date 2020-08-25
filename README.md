# FamPay API 
- Server should call the YouTube API continuously in background (async) with some interval (say 10 seconds) for fetching the latest videos for a predefined search query and should store the data of videos (specifically these fields - Video title, description, publishing datetime, thumbnails URLs and any other fields you require) in a database with proper indexes.

# Displaying all the videos in Paginated ListView
# Url  : http://127.0.0.1:8000/api/videos
![image](https://user-images.githubusercontent.com/21499789/91182615-02be4500-e708-11ea-85e8-598f665213ae.png)

# Searching Query in APIVideosList
# Url : http://127.0.0.1:8000/api/videos?search=covid
![image](https://user-images.githubusercontent.com/21499789/91182829-503ab200-e708-11ea-8bdf-7c52591d7c57.png)
