from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import Http404

# Create your views here.

from .models import Song, Entry, Detail
from .forms import SongForm, EntryForm, DetailForm

def index(request):
    """Home page"""
    return render(request, 'setlist/index.html')

@login_required
def songs(request):
    """Songs page"""
    songs = Song.objects.filter(owner=request.user)
    context = {'songs': songs}
    return render(request, 'setlist/songs.html', context)

@login_required
def song(request, song_id):
    """Specific song page"""
    song = Song.objects.get(id=song_id)
    #Make sure the song belongs to the current user
    if song.owner != request.user:
        raise Http404
    
    entries = song.entry_set.all()
    context = {'song': song, 'entries': entries}
    return render(request, 'setlist/song.html', context)

@login_required
def entry(request, song_id, entry_id):
    song = Song.objects.get(id=song_id)
    entry = Entry.objects.get(id=entry_id)
    if song.owner != request.user:
        raise Http404

    details = entry.detail_set.all()
    context = {'song': song, 'entry': entry, 'details': details}
    return render(request, 'setlist/entry.html', context)

@login_required  
def new_song(request):
    """Add a new song"""
    if request.method != 'POST':
        #No data submitted create blank form
        form = SongForm()
    else:
        #Post and process data given
        form = SongForm(data=request.POST)
        if form.is_valid():
            new_song = form.save(commit=False)
            new_song.owner = request.user
            new_song.save()
            return redirect('setlist:songs')

    #Display a blank or invalid form 
    context = {'form': form}
    return render(request, 'setlist/new_song.html', context)

@login_required
def new_entry(request, song_id):
    song = Song.objects.get(id=song_id)
    if request.method != 'POST':
        #Create blank form
        form = EntryForm()
    else:
        #Post and process data given
        form = EntryForm(data=request.POST)
        if form.is_valid():
            new_entry = form.save(commit=False)
            new_entry.song = song
            new_entry.save()
            return redirect('setlist:song', song_id=song_id)

    #Display blank/invalid form
    context = {'song': song, 'form': form}
    return render(request, 'setlist/new_entry.html', context)

@login_required
def new_detail(request, song_id, entry_id):
    song = Song.objects.get(id=song_id)
    entry = Entry.objects.get(id=entry_id)
    if request.method != 'POST':
        form = DetailForm()
    else:
        form = DetailForm(data=request.POST)
        if form.is_valid():
            new_detail = form.save(commit=False)
            new_detail.song = song
            new_detail.entry = entry
            new_detail.save()
            return redirect('setlist:entry', song_id=song_id, entry_id=entry_id)

    context = {'song': song, 'entry': entry, 'form': form}
    return render(request, 'setlist/new_detail.html', context)

@login_required
def edit_entry(request, song_id, entry_id):
    song = Song.objects.get(id=song_id)
    entry = Entry.objects.get(id=entry_id)
    if song.owner != request.user:
        raise Http404

    if request.method != 'POST':
        #Initial request, prefill form with existing entry
        form = EntryForm(instance=entry)
    else:
        #Post data submitted
        form = EntryForm(instance=entry, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('setlist:entry', song_id=song_id, entry_id=entry_id)

    context = {'song': song, 'entry': entry, 'form': form}
    return render(request, 'setlist/edit_entry.html', context)

@login_required
def edit_detail(request, song_id, entry_id, detail_id):
    song = Song.objects.get(id=song_id)
    entry = Entry.objects.get(id=entry_id)
    detail = Detail.objects.get(id=detail_id)
    if song.owner != request.user:
        raise Http404

    if request.method != 'POST':
        #Initial request, prefill form with exsisting detail
        form = DetailForm(instance=detail)
    else:
        #Post data submitted
        form = DetailForm(instance=detail, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('setlist:entry', song_id=song_id, entry_id=entry_id)

    context = {'song': song, 'entry': entry, 'detail': detail, 'form': form}
    return render(request, 'setlist/edit_detail.html', context)

@login_required
def delete_song(request, song_id):
    song = Song.objects.get(id=song_id)
    if song.owner != request.user:
        raise Http404

    if request.method == "POST":
        song.delete()
        return redirect('setlist:songs')

    context = {'song': song}
    return render(request, 'setlist/delete_song.html', context)

@login_required
def delete_entry(request, song_id, entry_id):
    song = Song.objects.get(id=song_id)
    entry = Entry.objects.get(id=entry_id)
    if song.owner != request.user:
        raise Http404
    
    if request.method == "POST":
      entry.delete()
      return redirect('setlist:song', song_id=song_id)

    context = {'song': song, 'entry': entry}
    return render(request, 'setlist/delete_entry.html', context)
