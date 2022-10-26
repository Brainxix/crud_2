from django.contrib import admin

# Register your models here.
from .models import lyric, song, artise

admin.site.register(artise)
admin.site.register(song)
admin.site.register(lyric)