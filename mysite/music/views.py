from django.shortcuts import render
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.views import View

from .models import *
from .forms import *

def index(request):
    """Список музыкальных групп"""
    bands = MusicBand.objects.all()
    return render(request, 'index.html', {'band': bands})


def show_album(request, band_id):
    """Список альбомов группы"""
    bands = MusicBand.objects.filter(id=band_id)
    albums = Album.objects.filter(band_id=band_id)
    context = {
        'albums': albums,
        'band_id': band_id,
        'bands': bands,
    }
    return render(request, 'band_info.html', context=context)


def show_track(request, album_id):
    """Список треков группы"""
    albums = Album.objects.filter(id=album_id)
    tracks = Track.objects.filter(album_id=album_id)
    context = {
        'tracks': tracks,
        'album_id': album_id,
        'albums': albums,
    }
    return render(request, 'album_info.html', context=context)






