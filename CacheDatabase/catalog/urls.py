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
    path('', views.home, name='home'),
]
