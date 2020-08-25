from django.conf.urls import url
from api import views

urlpatterns = [
    url('videos', views.APIVideosList.as_view(), name='videos'),
]
