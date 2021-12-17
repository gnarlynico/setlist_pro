from django.contrib import admin

# Register your models here.

from .models import Song, Entry, Detail

admin.site.register(Song)
admin.site.register(Entry)
admin.site.register(Detail)
