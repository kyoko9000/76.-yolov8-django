from django.urls import path

from yolos import views

urlpatterns = [
    path("", views.base, name="base"),
    path("yolo1/", views.video_feed, name="stream"),
    path("yolo2/", views.video_feed_1, name="stream_1")
]