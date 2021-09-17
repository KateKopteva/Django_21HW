from django.contrib import admin
from .models import *


# Register your models here.
@admin.register(MusicBand)
class MusicBandAdmin(admin.ModelAdmin):
    list_display = ['name', 'year', 'style']


@admin.register(Album)
class AlbumAdmin(admin.ModelAdmin):
    list_display = ['name_album', 'year_album']


@admin.register(Track)
class TrackAdmin(admin.ModelAdmin):
    list_display = ['name_track', 'time']