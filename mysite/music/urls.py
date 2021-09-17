from django.urls import path, re_path
from django.utils import archive
from . import views
from .views import *

urlpatterns = [
    path('', index, name='home'),
    path('band/<int:band_id>', show_album, name='band'),
    path('band/<int:band_id>/album/<int:album_id>', show_track, name='album'),
     ]