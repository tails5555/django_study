from django.shortcuts import render
from .models import Music
from .forms import MusicForm
# Create your views here.

def music_list(request) :
    musics = Music.objects.all()
    return render(request, 'music/list.html', {'musics' : musics})

def music_create(request) :
    music = MusicForm()
    return render(request, 'music/edit.html', {'form' : music})