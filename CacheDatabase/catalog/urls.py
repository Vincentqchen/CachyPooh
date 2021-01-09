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
    # path('', views.home, name="home"),
    # path('videos', views.videos, name='videos'),
    path('', views.home, name='home'),
    path('<media>/', views.media, name = 'media'),
    path('<media>/<category>/<vid_id>', views.finalVidView, name = 'finalVidView')
]


def demo(request):
    request = request
    template = "home/<media>.html"
    data = {}
    return render(request, template, data)