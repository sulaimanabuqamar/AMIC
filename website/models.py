from django.db import models

# Create your models here.

class Timeline(models.Model):
    timeline_id = models.AutoField(primary_key=True)
    activity_name = models.CharField(max_length=100)
    activity = models.TextField()
    date = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    
class headTeam(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    role = models.CharField(max_length=100)
    about = models.TextField()

class committeeTeam(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    role = models.CharField(max_length=100)
    about = models.TextField()
    amicoins = models.IntegerField(default=0)

class memberTeam(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    about = models.TextField()
    amicoins = models.IntegerField(default=0)
    
class advisorTeam(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    role = models.CharField(max_length=100)
    about = models.TextField()
