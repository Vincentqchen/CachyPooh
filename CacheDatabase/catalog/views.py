from django.shortcuts import render
from .models import *

import os
import json
import google_auth_oauthlib.flow
import googleapiclient.discovery
import googleapiclient.errors


# Create your views here.
def home(request):
    VideoObject = VideoYT.objects.filter(ytType__contains='mostPopular')[0]
    embed = 'https://www.youtube.com/embed/'+VideoObject.vidID
    return render(request, 'home.html', {'videos':VideoObject,'embed':embed})

def youtubeView(request):
    pass


    #return render(request, '')
