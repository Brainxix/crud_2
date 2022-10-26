
from django.db import models
from datetime import datetime

# Create your models here.
class artise(models.Model):
    first_name = models.CharField(max_length = 500)
    last_name = models.CharField(max_length = 500)
    age =models.IntegerField()

    def __str__(self):
        return self.first_name


class song(models.Model):
    artise = models.ForeignKey(artise, on_delete=models.CASCADE)
    title = models.CharField(max_length= 300)
    date_released = models.DateTimeField(default=datetime.today)
    likes = models.IntegerField()
    artiste_id = models.IntegerField()

def __str__(self):
    return self.artise
    

class lyric(models.Model):
    song = models.ForeignKey(song, on_delete = models.CASCADE )
    content = models.CharField(max_length = 500)
    Song_id = models.BooleanField()