from django.db import models

# Create your models here.


class Activity(models.Model):
    activity_id = models.AutoField(primary_key=True)
    activity_name = models.CharField(max_length=100)
    activity = models.TextField()
    date = models.CharField(max_length=100)
    location = models.CharField(max_length=100, null=True,blank=True)
class Timeline(models.Model):
    timeline_id = models.AutoField(primary_key=True)
    start_year = models.CharField(max_length=4,default="2024")
    end_year = models.CharField(max_length=4,default="2025")
    activities = models.ManyToManyField("Activity", blank=True)
    
class head(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    role = models.CharField(max_length=100)
    about = models.TextField()
    TEAM_TYPES = (
        ('highschool', 'High School'),
        ('junior', 'Junior'),
        ('alumni', 'Alumni'),
    )
    team_type = models.CharField(max_length=10, choices=TEAM_TYPES, default='highschool')

class committee(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    role = models.CharField(max_length=100)
    about = models.TextField()
    amicoins = models.IntegerField(default=0)
    TEAM_TYPES = (
        ('highschool', 'High School'),
        ('junior', 'Junior'),
        ('alumni', 'Alumni'),
    )
    team_type = models.CharField(max_length=10, choices=TEAM_TYPES, default='highschool')

class member(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    about = models.TextField()
    amicoins = models.IntegerField(default=0)
    TEAM_TYPES = (
        ('highschool', 'High School'),
        ('junior', 'Junior'),
        ('alumni', 'Alumni'),
    )
    team_type = models.CharField(max_length=10, choices=TEAM_TYPES, default='highschool')
    
class advisor(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    role = models.CharField(max_length=100)
    about = models.TextField()
    
class Photo(models.Model):
    activity = models.ForeignKey(Activity, on_delete=models.CASCADE, related_name='photos', null=True)
    image = models.ImageField(upload_to='timeline_photos/')

class aboutUsPhoto(models.Model):
    image1 = models.ImageField(upload_to='about_us_photos/')
    image2 = models.ImageField(upload_to='about_us_photos/')
    image3 = models.ImageField(upload_to='about_us_photos/')