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
            post = post_form.save()
            wysiwyg = wysiwyg_form.save(commit = False)
            wysiwyg.post = post
            wysiwyg.save()
            return redirect('post_list')

    else :
        post_form = PostForm()
        wysiwyg_form = WysiwygForm()

    return render(request, 'post/edit.html', {'post_form' : post_form, 'wysiwyg_form' : wysiwyg_form, 'message' : '등록'})

def post_view(request, id) :
    if id != 0 :
        post = Post.objects.filter(id=id).first()
        if post != None :
            wysiwyg = Wysiwyg.objects.get(post = post)
            return render(request, 'post/view.html', {'view' : wysiwyg })
        else :
            return render(request, 'post/error.html')
    
    else :
        return render(request, 'post/error.html')

def post_update(request, id) :
    if id != 0 :
        tmp_post = Post.objects.filter(id=id).first()

        if tmp_post != None :
            tmp_wysiwyg = Wysiwyg.objects.get(post=tmp_post)
            
            if tmp_wysiwyg != None :
                post_form = PostForm(request.POST or None, instance=tmp_post)
                wysiwyg_form = WysiwygForm(request.POST or None, instance=tmp_wysiwyg)

                if post_form.is_valid() and wysiwyg_form.is_valid() :
                    post = post_form.save()
                    wysiwyg = wysiwyg_form.save(commit = False)
                    wysiwyg.post = post
                    wysiwyg.save()
                    return redirect('post_list')

            else :
                return render(request, 'post/error.html')

        else :
            return render(request, 'post/error.html')

        return render(request, 'post/edit.html', {'post_form' : post_form, 'wysiwyg_form' : wysiwyg_form, 'message' : '수정', 'id' : id})

    else :
        return render(request, 'post/error.html')

def post_delete(request, id) :
    if id != 0 :
        tmp_post = Post.objects.filter(id=id).first()

        if tmp_post != None :
            Post.objects.filter(pk=id).delete()
            return redirect('post_list')
    
        else :
            post_form = PostForm()
            wysiwyg_form = WysiwygForm()

        return render(request, 'post/edit.html', {'post_form' : post_form, 'wysiwyg_form' : wysiwyg_form, 'message' : '수정'})

    else :
        return render(request, 'post/error.html')