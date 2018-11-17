from django.shortcuts import render
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from .forms import SignForm
from .models import Job, Account

def sign_up(request):
    if request.method == 'POST':
        form = SignForm(request.POST)
        
        if form.is_valid():
            user = form.save(commit=False)
            tmp_username = form.cleaned_data.get('username')
            tmp_password = form.cleaned_data.get('password')
            user.set_password(tmp_password)
            user.save()
            user.refresh_from_db()
            
            tmp_account = Account.objects.filter(user=user).first()
            
            if tmp_account != None :
                tmp_job_id = form.cleaned_data.get('job')
                tmp_account.job = Job.objects.get(id=tmp_job_id)
                tmp_account.address = form.cleaned_data.get('address')
                tmp_account.birthday = form.cleaned_data.get('birthday')
                tmp_account.save()

                return redirect('login_page')
            
            else :
                return render(request, 'guest/sign_up.html', { 'form' : form })
        
        else :
            return render(request, 'guest/sign_up.html', { 'form' : form })
    
    else:
        form = SignForm()
    
    return render(request, 'guest/sign_up.html', { 'form' : form })