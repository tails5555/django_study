from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from urllib.parse import parse_qs
from .models import Post, Type, Wysiwyg
from .forms import PostForm, WysiwygForm
from django.shortcuts import redirect

def index(request) :
    return render(request, 'home.html')

def post_list(request) :
    posts = Post.objects.all()
    return render(request, 'post/list.html', {'posts' : posts})

def post_create(request) :
    if request.method == "POST":
        post_form = PostForm(request.POST)
        wysiwyg_form = WysiwygForm(request.POST)

        if post_form.is_valid() and wysiwyg_form.is_valid() :
            post_form.save()
            return redirect('post_list')

    else :
        post_form = PostForm()
        wysiwyg_form = WysiwygForm()

    return render(request, 'post/edit.html', {'post_form' : post_form, 'wysiwyg_form' : wysiwyg_form, 'message' : '등록'})

def post_update(request) :
    post_id = int(request.GET.get('id'))
    tmp_post = Post.objects.get(pk=post_id)
    post_form = PostForm(request.POST or None, instance=tmp_post)
    wysiwyg_form = WysiwygForm(request.POST or None, instance=tmp_post.context)

    if post_form.is_valid() and wysiwyg_form.is_valid() :
        wysiwyg_form.save()
        post_form.save()
        return redirect('post_list')

    return render(request, 'post/edit.html', {'post_form' : post_form, 'wysiwyg_form' : wysiwyg_form, 'message' : '수정', 'id' : post_id})