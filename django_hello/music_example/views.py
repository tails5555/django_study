from django.shortcuts import render
from urllib.parse import parse_qs
from .models import Music, Genre
from .forms import MusicForm, GenreForm
from django.shortcuts import redirect

def index(request) :
    return render(request, 'index.html')

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

def genre_list(request) :
    genres = Genre.objects.all()
    return render(request, 'genre/list.html', {'genres' : genres})

def genre_create(request) :
    if request.method == "POST":
        genre_form = GenreForm(request.POST)

        if genre_form.is_valid() :
            genre_form.save()
            return redirect('genre_list')

    else :
        genre_form = GenreForm()

    return render(request, 'genre/edit.html', {'form' : genre_form, 'message' : '등록'})

def genre_update(request, id) :
    tmp_genre = Genre.objects.get(pk=id)
    genre_form = GenreForm(request.POST or None, instance=tmp_genre)
    music_list = Music.objects.filter(genre=tmp_genre)

    if genre_form.is_valid() :
        genre_form.save()
        return redirect('genre_list')

    return render(request, 'genre/edit.html', {'form' : genre_form, 'message' : '수정', 'musics' : music_list, 'id' : id})

def genre_delete(request, id) :
    if id != 0 :
        tmp_genre = Genre.objects.get(pk=id)
        music_list = Music.objects.filter(genre=tmp_genre)
        genre_form = GenreForm(request.POST or None, instance=tmp_genre)
        Genre.objects.filter(pk=id).delete()
        return redirect('genre_list')
    
    else :
        genre_form = GenreForm()

    return render(request, 'genre/edit.html', {'form' : genre_form, 'message' : '수정', 'musics' : music_list, 'id' : id})