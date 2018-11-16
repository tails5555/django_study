from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from urllib.parse import parse_qs
from .models import Post, Type, Wysiwyg
from .forms import PostForm, WysiwygForm
from django.shortcuts import redirect
from django.http import QueryDict
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

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
            return render(request, 'error.html')
    
    else :
        return render(request, 'error.html')

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
                return render(request, 'error.html')

        else :
            return render(request, 'error.html')

        return render(request, 'post/edit.html', {'post_form' : post_form, 'wysiwyg_form' : wysiwyg_form, 'message' : '수정', 'id' : id})

    else :
        return render(request, 'error.html')

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
        return render(request, 'error.html')

def type_list(request, **kwargs) :
    types = Type.objects.all()
    type_id = int(request.GET.get('type'))
    tmp_type = Type.objects.filter(id=type_id).first()

    if tmp_type != None :
        pg = request.GET.get('pg')
        st = request.GET.get('st')
        sb = request.GET.get('sb')
        ob = request.GET.get('ob')

        if sb == '1' :
            post_list = Post.objects.filter(type=tmp_type, title__icontains=st)
        elif sb == '2' :
            post_list = Post.objects.filter(type=tmp_type, writer=st)
        elif sb == '3' :
            post_list = Post.objects.filter(type=tmp_type, title__icontains=st, context__icontains=st)
        else :
            post_list = Post.objects.filter(type=tmp_type)

        if ob == '0' or ob == '1' :
            post_list = post_list.order_by('-id')
        elif ob == '2' :
            post_list = post_list.order_by('id')
        elif ob == '3' :
            post_list = post_list.order_by('title')
        elif ob == '4' :
            post_list = post_list.order_by('-title')
        else :
            post_list = post_list

        paginator = Paginator(post_list, 8)
        totalPageCount = paginator.num_pages
        
        try:
            posts = paginator.page(pg)
        except PageNotAnInteger:
            posts = paginator.page(1)
        except EmptyPage:
            posts = paginator.page(paginator.num_pages)

        startPageNum = (( int(pg) - 1 ) // 10 ) * 10
        endPageNum = startPageNum + 11

        if endPageNum > totalPageCount :
            endPageNum = totalPageCount + 1
        
        bottomPages = range(startPageNum + 1, endPageNum)

        page_query = request.GET.copy()
        del page_query['pg']

        return render(request, 'type/list.html', { 'posts' : posts, 'types' : types, 'query' : request.GET.urlencode(), 'page_query' : page_query.urlencode(), 'start' : startPageNum, 'end' : endPageNum, 'middle' : bottomPages, 'total' : totalPageCount })

    else :
        return render(request, 'type/list.html', { 'posts' : [], 'types' : types, 'query' : request.GET.urlencode() })

def type_view(request) :
    types = Type.objects.all()
    post_id = int(request.GET.get('id'))

    if post_id != 0 :
        if not request.GET._mutable :
            request.GET._mutable = True
            request.GET.pop('id')
        
        post = Post.objects.filter(id=post_id).first()

        if post != None :
            wysiwyg = Wysiwyg.objects.get(post = post)
            return render(request, 'type/view.html', { 'view' : wysiwyg, 'query' : request.GET.urlencode(), 'types' : types })
        else :
            return render(request, 'error.html')
    
    else :
        return render(request, 'error.html')

