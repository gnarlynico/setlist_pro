"""URL patterns for setlist"""

from django.urls import path

from . import views

app_name = 'setlist'
urlpatterns = [
    #Home page
    path('', views.index, name='index'),
    #All songs page
    path('songs/', views.songs, name='songs'),
    #Specific song page
    path('songs/<int:song_id>/', views.song, name='song'),
    #Specific entry about a specific song page
    path('songs/<int:song_id>/<int:entry_id>/', views.entry, name='entry'),
    #Page for adding a new song
    path('new_song/', views.new_song, name='new_song'),
    #Page for new entries
    path('new_entry/<int:song_id>/', views.new_entry, name='new_entry'),
    #Page for adding new entry detail
    path('new_detail/<int:song_id>/<int:entry_id>/', views.new_detail,
         name='new_detail'),
    #Page for editing an entry name
    path('edit_entry/<int:song_id>/<int:entry_id>/', views.edit_entry,
         name='edit_entry'),
    #Page for editing exsisting entry detail
    path('edit_detail/<int:song_id>/<int:entry_id>/<int:detail_id>/',
         views.edit_detail, name='edit_detail'),
    #Page for deleting song
    path('<int:song_id>/delete/', views.delete_song, name='delete_song'),
    #Page for deleting entry
    path('<int:song_id>/<int:entry_id>/delete/', views.delete_entry,
         name='delete_entry'),
]
