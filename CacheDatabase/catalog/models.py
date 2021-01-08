from django.db import models
import os
#Google api
import json
from googleapiclient.discovery import build
#Scheduler
from apscheduler.schedulers.background import BackgroundScheduler

class YoutubeCache(models.Model):
    def __str__(self):
        return "hi"
class Video(models.Model):
    youtube_cache = models.ForeignKey(YoutubeCache,on_delete=models.CASCADE)
    url = models.TextField(max_length=600, null=False, blank=False)
    title = models.TextField(max_length=600, null=False, blank=False)
    length = models.IntegerField(max_length=100, null=False, blank=False)
    views = models.IntegerField(max_length=15, null=False, blank=False)
    date = models.DateField(auto_now=False, auto_now_add=False)
    ytType = models.CharField(max_length=30, null=False, blank=False)


# Create your models here.

def ytCacheHelper():
    youtube = build('youtube','v3',developerKey = 'AIzaSyBVb4q7yTC3-Gx7qAWIvPaeZUnJuUc6HkU')

    YTrequest = youtube.videos().list(
        part="snippet",
        chart="mostPopular",
        regionCode="US"
    )
    response = YTrequest.execute()

    # YTresponse

#Schedule daily database updates
scheduler = BackgroundScheduler()
scheduler.add_job(ytCacheHelper, 'interval', seconds=3)
scheduler.start()