from django.db import models
import os
from datetime import datetime 
#Google api
import json
from googleapiclient.discovery import build
#Scheduler
from apscheduler.schedulers.background import BackgroundScheduler

# class YoutubeCache(models.Model):
#     def __str__(self):
#         return "hi"

class Video(models.Model):
    #youtube_cache = models.ForeignKey(YoutubeCache,on_delete=models.CASCADE)
    url = models.CharField(max_length=600, null=False, blank=False)
    title = models.CharField(max_length=600, null=False, blank=False)
    length = models.CharField(max_length=600, null=False, blank=False)
    views = models.IntegerField(max_length=15, null=False, blank=False)
    date = models.DateField(auto_now=False, auto_now_add=False)
    ytType = models.CharField(max_length=30, null=False, blank=False)


# Create your models here.

def ytCacheHelper():
    youtube = build('youtube','v3',developerKey = 'AIzaSyBVb4q7yTC3-Gx7qAWIvPaeZUnJuUc6HkU')

    #Most popular videos in the us
    YTrequest = youtube.videos().list(
        part="snippet,contentDetails,statistics",
        chart="mostPopular",
        regionCode="US"
    )
    response = YTrequest.execute()
    #Python dictionary of all top yt videos
    items = response['items']
    for x in range(len(items)):
        # Parts of video
        snippet = items[x]['snippet']
        contentDetails = items[x]['contentDetails']
        statistics = items[x]['statistics']
        print(snippet['title'])

        # Figure out length of video
        length = contentDetails['duration']
        length = length[2:]
        #Figure out date of video
        date = snippet['publishedAt']
        year = int(date[:4])
        month = int(date[5:7])
        day = int(date[8:10])
        hour = int(date[11:13])
        minute = int(date[14:16])
        date = datetime(year, month, day, hour, minute)
        #date = datetime.fromisoformat(date)
        # Set up the video model
        mostViewedVideo = Video(url='https://www.youtube.com/watch?v='+items[x]['id'], title=snippet['title'], length=length, views=statistics['viewCount'], date=date, ytType='mostPopular')
        mostViewedVideo.save()
    

ytCacheHelper()
#Schedule daily database updates
# scheduler = BackgroundScheduler()
# scheduler.add_job(ytCacheHelper, 'interval', seconds=3)
# scheduler.start()