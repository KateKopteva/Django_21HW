from django.conf import settings
from django.db import models
from django.urls import reverse



class Album(models.Model):
    name_album = models.CharField(max_length=255, verbose_name='Название альбома')
    year_album = models.DateField(verbose_name='Год выпуска')
    band = models.ForeignKey('MusicBand', verbose_name='Группа', null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.name_album

    def get_absolute_url(self):
        return reverse('album', kwargs={'album_id': self.pk})



class MusicBand(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название группы')
    year = models.DateField(verbose_name='Год основания')
    style = models.CharField(max_length=255, verbose_name='Жанр')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('band', kwargs={'band_id': self.pk})



class Track(models.Model):
    name_track = models.CharField(max_length=255, verbose_name='Название трека')
    time = models.DurationField(verbose_name='Длительность трека')
    album = models.ForeignKey('Album', verbose_name='Альбом', null=True, on_delete=models.SET_NULL)







