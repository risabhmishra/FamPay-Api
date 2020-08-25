# FamPay API 
- Server should call the YouTube API continuously in background (async) with some interval (say 10 seconds) for fetching the latest videos for a predefined search query and should store the data of videos (specifically these fields - Video title, description, publishing datetime, thumbnails URLs and any other fields you require) in a database with proper indexes.

# Prequisites - Python 3.5+
1. Install Pip - sudo apt install python3-pip
2. git clone this respository
3. create a virtual environment and activate it
4. Install all the required dependencies and libraries - pip3 install -r requirements.txt

# Prequisites Postgres Database
1. sudo apt install postgresql 
2. It is necessary that you execute the commands below and create a user:
      1.  sudo su - postgres 
      2. postgres@ubuntu:~$ psql 
      3. postgres=# create role <username> with password '<password>' createdb login;

## Modify settings :
1. The database username and password must be set before running the web app.
2. cd FamPayAssignment/FamPayAssignment
3. open the __settings.py__ file and change the username and password in "DATABASES".
4. Specify the username and password that was set for the database.
5. Set DEVELOPER_KEY to the API key value from the APIs & auth > Registered apps

## Running FamPay Api :
1. python3 manage.py makemigrations
2. python3 manage.py migrate
3 python3 manage.py runserver

# Displaying all the videos in Paginated ListView
- Url  : http://127.0.0.1:8000/api/videos
![image](https://user-images.githubusercontent.com/21499789/91182615-02be4500-e708-11ea-85e8-598f665213ae.png)

# Searching Query in APIVideosList
- Url : http://127.0.0.1:8000/api/videos?search=covid
![image](https://user-images.githubusercontent.com/21499789/91182829-503ab200-e708-11ea-8bdf-7c52591d7c57.png)
