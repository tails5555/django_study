from django.shortcuts import render
from urllib.parse import parse_qs
from .models import Music, Genre
from .forms import MusicForm
from django.shortcuts import redirect

def music_list(request) :
    musics = Music.objects.all()
    return render(request, 'music/list.html', {'musics' : musics})

def music_create(request) :
    if request.method == "POST":
        music_form = MusicForm(request.POST)

        if music_form.is_valid() :
            music_form.save()
            return redirect('music_list')

    else :
        music_form = MusicForm()

    return render(request, 'music/edit.html', {'form' : music_form, 'message' : '등록'})

def music_update(request) :
    music_id = int(request.GET.get('id'))
    tmp_music = Music.objects.get(pk=music_id)
    music_form = MusicForm(request.POST or None, instance=tmp_music)
    
    if music_form.is_valid() :
        music_form.save()
        return redirect('music_list')

    return render(request, 'music/edit.html', {'form' : music_form, 'message' : '수정', 'id' : music_id})

def music_delete(request) :
    music_id = int(request.GET.get('id'))
    
    if music_id != 0 :
        tmp_music = Music.objects.get(pk=music_id)
        music_form = MusicForm(request.POST or None, instance=tmp_music)
        Music.objects.filter(pk=music_id).delete()
        return redirect('music_list')
    
    else :
        music_form = MusicForm()

    return render(request, 'music/edit.html', {'form' : music_form, 'message' : '수정', 'id' : music_id})