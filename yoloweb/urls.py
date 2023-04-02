from django.urls import path

from yoloweb.views import base, video_feed

urlpatterns = [
    path("", base, name="base"),
    path("yolo/", video_feed, name="stream")
]