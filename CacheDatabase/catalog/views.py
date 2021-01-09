from django.shortcuts import render
from .models import *

import os
import json
import google_auth_oauthlib.flow
import googleapiclient.discovery
import googleapiclient.errors


# Create your views here.
def home(request):



    VideoObjects = VideoYT.objects.filter(ytType__contains='mostPopular')
    VideoObject = VideoObjects[len(VideoObjects)-1]
    embed = 'https://www.youtube.com/embed/'+VideoObject.vidID
    return render(request, 'home.html', {'videos':VideoObject,'embed':embed})

def media(request, media):
    if media == 'youtube':
        popularVideos = VideoYT.objects.filter(ytType__contains='mostPopular')
        return render(request, 'media.html', {'popularVids':popularVideos})
    elif media == 'twitter':
        pass
    elif media == 'instagram':
        pass

def finalVidView(request, media, category, vid_id):
    VideoObjects = VideoYT.objects.filter(ytType__contains='mostPopular')
    VideoObject = VideoObjects[len(VideoObjects)-1]
    embed = 'https://www.youtube.com/embed/'+VideoObject.vidID
    return render(request, 'home.html', {'videos':VideoObject,'embed':embed, 'videos'})
