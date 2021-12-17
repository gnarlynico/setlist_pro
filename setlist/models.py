from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Song(models.Model):
    """A song user wants to add"""
    text = models.CharField(max_length=200)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.text

class Entry(models.Model):
    """Info category about a song"""
    song = models.ForeignKey(Song, on_delete=models.CASCADE)
    text = models.CharField(max_length=200)

    class Meta:
        verbose_name_plural = 'entries'

    def __str__(self):
        return self.text

class Detail(models.Model):
    """Details of an entry"""
    entry = models.ForeignKey(Entry, on_delete=models.CASCADE)
    text = models.TextField()

    class Meta:
        verbose_name_plural = 'details'

    def __str__(self):
        return f"{self.text[:30]}..."
