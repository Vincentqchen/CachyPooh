from django.urls import path
from . import views
from datetime import datetime
from .models import *
#Google api
import json
from googleapiclient.discovery import build
#Scheduler
from apscheduler.schedulers.background import BackgroundScheduler


urlpatterns = [
    path('', views.home, name="home"),
    path('videos', views.videos, name='videos'),
]


def demo(request):
    request = request
    template = "home/<media>.html"
    data = {}
    return render(request, template, data)