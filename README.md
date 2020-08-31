# YouTube Search API 
- Server should call the YouTube API continuously in background (async) with some interval (say 10 seconds) for fetching the latest videos for a predefined search query and should store the data of videos (specifically these fields - Video title, description, publishing datetime, thumbnails URLs and any other fields you require) in a database with proper indexes.

# Technology Stack
- Api : Django Rest Framework
- Asysnchronous Background Task Processing : Celery and Redis
- Database : PostgreSQL

# Prequisites - Python 3.5+
1. Install Pip - sudo apt install python3-pip
2. git clone this respository
3. create a virtual environment and activate it
4. Install all the required dependencies and libraries - pip3 install -r requirements.txt

# Setting up PostgreSQL Database
1. sudo apt install postgresql 
2. It is necessary that you execute the commands below and create a user:
      1.  sudo su - postgres 
      2. postgres@ubuntu:~$ psql 
      3. postgres=# create role <username> with password '<password>' createdb login;
      
# Setting up Celery and Redis server
1. pip install celery==3.1.18
2. pip install redis==2.10.3
3. Redis Server : sudo apt-get install redis-server

Configure Redis as a cache on Ubuntu

To configure Redis as a cache you need to edit the /etc/redis/redis.conf file. We will use nano as a text editor for this purpose, but you can use any text editor of your choice.
- sudo nano /etc/redis/redis.conf

To configure the max memory for Redis as well as how Redis will select what to remove when the max memory is reached, add the following lines at the end of the file:
- maxmemory 128mb
- maxmemory-policy allkeys-lru

In this example, Redis will remove any key according to the LRU algorithm when the max memory of 128mb is reached. Save and close the file, then restart the Redis service:
- sudo systemctl restart redis-server.service

Next, enable Redis on system boot:
- sudo systemctl enable redis-server.service

# Running Celery Commands in two different terminals
1. celery -A clmsite worker -l info
2. celery -A clmsite beat -l info

## Modify settings :
1. The database username and password must be set before running the web app.
2. cd youtubeapi/youtubeapi
3. open the __settings.py__ file and change the username and password in "DATABASES".
4. Specify the username and password that was set for the database.
5. Set DEVELOPER_KEY to the API key value from the APIs & auth > Registered apps.
6. Set QUERY_TERM to 'search_query' to be searched in the YouTube Data Api.

## Running Api :
1. python3 manage.py makemigrations
2. python3 manage.py migrate
3 python3 manage.py runserver

# Displaying all the videos in Paginated ListView
- Url  : http://127.0.0.1:8000/api/videos
![image](https://user-images.githubusercontent.com/21499789/91182615-02be4500-e708-11ea-85e8-598f665213ae.png)

# Searching Query in APIVideosList
- Url : http://127.0.0.1:8000/api/videos?search=covid
![image](https://user-images.githubusercontent.com/21499789/91182829-503ab200-e708-11ea-8bdf-7c52591d7c57.png)
