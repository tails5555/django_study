from django import forms
from django.forms.widgets import Select
from django_summernote import fields as summer_fields
from .models import Post, Type, Wysiwyg

class PostForm(forms.ModelForm) :
    class Meta :
        model = Post
        fields = ('type', 'title')
    
    def __init__(self, *args, **kwargs):
        super(PostForm, self).__init__(*args, **kwargs)
        for key in ('type', 'title'):
               self.fields[key].widget.attrs.update({
                    'class': 'form-control w200'
                })

        self.fields['type'].label = '게시판 종류'
        self.fields['type'].choices = [(t.id, t.name) for t in Type.objects.all()]
        self.fields['title'].label = '제목'
        

class WysiwygForm(forms.ModelForm) :
    class Meta :
        model = Wysiwyg
        fields = ('wysiwyg_field',)

    def __init__(self, *args, **kwargs) :
        super(WysiwygForm, self).__init__(*args, **kwargs)
        self.fields['wysiwyg_field'] = summer_fields.SummernoteTextFormField(error_messages={ 'required' : ('게시글 내용을 입력해주세요.'), })
        self.fields['wysiwyg_field'].label = '내용'