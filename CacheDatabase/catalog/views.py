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
        gamingVids = VideoYT.objects.filter(ytType__icontains='Gaming')
        sportVids = VideoYT.objects.filter(ytType__icontains='Sport')
        musicVids = VideoYT.objects.filter(ytType__icontains='Music')
        data = {'gamingVids':gamingVids, 'sportVids':sportVids, 'musicVids':musicVids, }
        return render(request, 'youtube.html', data)
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
        VideoObjects = VideoYT.objects.filter(ytType__icontains=category, date__contains=datetime)
        embed = 'https://www.youtube.com/embed/'+VideoObject.vidID
        print('length: '+str(len(VideoObjects)))

        current_path = ""
        for x in request.build_absolute_uri().split(media+"/"+category+"/"):
            current_path += x
            break

        current_path = current_path+media+"/"+category+"/"

        data = {'video': VideoObject, 'embed': embed, 'videos': VideoObjects, 'current_path': current_path}

        return render(request, 'videos.html', data)
    elif media == 'twitter':
        pass
    elif media == 'instagram':
        pass
