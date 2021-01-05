from django.db import models

class YoutubeCache(models.Model):
    def __str__(self):
        return "hi"
class Video(models.Model):
    youtube_cache = models.ForeignKey(YoutubeCache,on_delete=models.CASCADE)
    url = models.CharField(max_length=600, null=False, blank=False)
    title = models.CharField(max_length=600, null=False, blank=False)
    length = models.IntegerField(max_length=100, null=False, blank=False)
    views = models.IntegerField(max_length=15, null=False, blank=False)
    date = models.DateField(auto_now=False, auto_now_add=False)
    ytType = models.CharField(max_length=30, null=False, blank=False)
# Create your models here.
