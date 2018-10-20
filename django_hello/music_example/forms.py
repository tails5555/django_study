from django import forms
from django.forms.widgets import Select
from .models import Music, Genre

class MusicForm(forms.ModelForm) :
    class Meta :
        model = Music
        fields = ('title', 'singer', 'genre', 'year',)
    
    def __init__(self, *args, **kwargs):
        super(MusicForm, self).__init__(*args, **kwargs)
        for key in ('title', 'singer', 'year', 'genre'):
               self.fields[key].widget.attrs.update({
                    'class': 'form-control w200'
                })

        self.fields['title'].label = '제목'
        self.fields['singer'].label = '가수'
        self.fields['year'].label = '발매 연도'
        self.fields['genre'].label = '장르'
        print(Genre.objects.all().only('id', 'name'))
        self.fields['genre'].choices = [(g.id, g.name) for g in Genre.objects.all()]

class GenreForm(forms.ModelForm) :
    class Meta :
        model = Genre
        fields = ('name',)

    def __init__(self, *args, **kwargs):
        super(GenreForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({
            'class': 'form-control w200'
        })
        self.fields['name'].label = '장르 이름'
    