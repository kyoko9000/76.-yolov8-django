from django.urls import path

from yoloweb import views

urlpatterns = [
    path("", views.base, name="base"),
    path("yolo", views.video_feed, name="stream")
]