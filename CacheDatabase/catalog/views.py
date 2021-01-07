from django.shortcuts import render
from .models import *

import os
import json
import google_auth_oauthlib.flow
import googleapiclient.discovery
import googleapiclient.errors


# Create your views here.
def index(request):
    return render(request, 'home.html', {})

def youtubeView(request):
    pass


    #return render(request, '')
