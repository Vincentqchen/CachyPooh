from django.shortcuts import render
from .models import *

import os
import json
import google_auth_oauthlib.flow
import googleapiclient.discovery
import googleapiclient.errors


# Create your views here.
def home(request):
    return render(request, 'home.html', {})

def media(request, media):
    if media == 'youtube':
        gamingVids = VideoYT.objects.filter(ytType__contains='Gaming')
        sportVids = VideoYT.objects.filter(ytType__contains='Sport')
        musicVids = VideoYT.objects.filter(ytType__contains='Music')
        return render(request, 'youtube.html', {'gamingVids':gamingVids,'sportVids':sportVids,'musicVids':musicVids})
    elif media == 'twitter':
        pass
    elif media == 'instagram':
        pass
    
    return render(request, 'index.html', {})

def finalView(request, media, category, vid_id):
    # If the media page is on youtube
    if media == 'youtube':
        # Single video to display
        VideoObject = VideoYT.objects.filter(vidID__contains=vid_id)[0]
        # All videos under the category and date of the video
        print(VideoObject.date)
        datetime = VideoObject.date
        VideoObjects = VideoYT.objects.filter(ytType__contains=category, date__contains=datetime)
        embed = 'https://www.youtube.com/embed/'+VideoObject.vidID
        return render(request, 'videos.html', {'video':VideoObject,'embed':embed, 'videos':VideoObjects})
    elif media == 'twitter':
        pass
    elif media == 'instagram':
        pass
