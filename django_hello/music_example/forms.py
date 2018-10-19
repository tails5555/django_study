from django import forms
from django.forms.widgets import Select
from .models import Music, Genre

class MusicForm(forms.ModelForm) :
    class Meta :
        model = Music
        choices = Genre.objects.all()
        fields = ('title', 'singer', 'genre', 'year',)
        widgets = {
            'genre': Select(choices=((x.id, x.name) for x in choices)),
        }
    
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