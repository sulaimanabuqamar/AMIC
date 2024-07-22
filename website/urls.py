from django.urls import path
from website import views

urlpatterns = [
    path("", views.Home, name="home"),
    path("About/", views.About, name="about"),
    path("Team/Highschool", views.team_Highschool, name="team_highschool"),
    path("Team/Junior", views.team_Junior, name="team_junior"),
    path("Team/Alumni", views.team_Alumni, name="team_alumni"),
    path("Leaderboard/", views.Leaderboard, name="leaderboard"),
    path("Contact/", views.Contact, name="contact"),
    path('Timeline/<int:timeline_id>/', views.timelineDetail, name='timeline_detail'),
    path('Activity/<int:activity_id>/', views.activity_detail, name='activity_detail'),
]