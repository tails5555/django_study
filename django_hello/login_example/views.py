from django.shortcuts import render
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from .forms import SignForm
from .models import Job

def sign_up(request):
    if request.method == 'POST':
        form = SignForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            tmp_password = form.cleaned_data.get('password')
            user.set_password(tmp_password)
            user.save()
            user.refresh_from_db()

            user.account.birthday = form.cleaned_data.get('birthday')
            tmp_job_id = form.cleaned_data.get('job')
            tmp_job = Job.objects.filter(id=tmp_job_id).first()
            
            if tmp_job != None :
                user.account.job = tmp_job
            else :
                return render(request, 'guest/sign_up.html', { 'form' : form })
            
            user.account.address = form.cleaned_data.get('address')
            user.save()

            return redirect('home')
        else :
            return render(request, 'guest/sign_up.html', { 'form' : form })
    else:
        form = SignForm()
    return render(request, 'guest/sign_up.html', { 'form' : form })