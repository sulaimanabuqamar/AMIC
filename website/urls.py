from django.urls import path
from website import views

urlpatterns = [
    path("", views.Home, name="home"),
    path("About/", views.About, name="about"),
    path("Timeline/", views.timelineDetail, name="timeline"),
    path("Team/", views.teamDetail, name="team"),
]