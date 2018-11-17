from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms.widgets import Select, SelectDateWidget, PasswordInput
from .models import Job
from datetime import date

class SignForm(forms.ModelForm) :
    password = forms.CharField(widget=PasswordInput)
    password_confirm = forms.CharField(widget=PasswordInput)
    job_choices = [(j.id, j.name) for j in Job.objects.all()]
    job = forms.ChoiceField(widget=Select, choices=job_choices)
    YEARS = [x for x in range(1940, 2018)]
    birthday = forms.DateField(widget=SelectDateWidget(years=YEARS))
    address = forms.CharField(max_length=100)

    class Meta :
        model = User
        fields = ('username', 'password', 'password_confirm', 'first_name', 'last_name', 'email', 'address', 'birthday', 'job')

    def clean(self):
        username = self.cleaned_data.get('username')
        password1 = self.cleaned_data.get('password')
        password2 = self.cleaned_data.get('password_confirm')
        first_name = self.cleaned_data.get('first_name')
        last_name = self.cleaned_data.get('last_name')
        email = self.cleaned_data.get('email')
        birthday = self.cleaned_data.get('birthday')

        username_qs = User.objects.filter(username=username)

        if username_qs.exists() :
            self.add_error('username', '회원이 이미 존재합니다.')

        if password1 != password2 :
            self.add_error('password', '비밀번호가 일치하지 않습니다.')

        if first_name == None :
            self.add_error('first_name', '이름을 입력하세요.')
        elif first_name.strip() == '' :
            self.add_error('first_name', '이름을 입력하세요.')

        if last_name == None  :
            self.add_error('last_name', '성을 입력하세요.')
        elif last_name.strip() == '' :
            self.add_error('last_name', '성을 입력하세요.')

        if email.strip() == '' :
            self.add_error('email', 'E-Mail을 입력하세요.')

        if birthday > date.today() :
            self.add_error('birthday', '오늘 날짜 이전으로 입력하시길 바랍니다.')

    def __init__(self, *args, **kwargs):
        super(SignForm, self).__init__(*args, **kwargs)
        for key in ('username', 'password', 'password_confirm', 'first_name', 'last_name', 'email', 'address', 'birthday', 'job'):
            self.fields[key].widget.attrs.update({
                'class': 'form-control w200'
            })

        self.fields['username'].label = '아이디'
        self.fields['password'].label = '비밀번호'
        self.fields['password_confirm'].label = '비밀번호 확인'
        self.fields['first_name'].label = '이름'
        self.fields['last_name'].label = '성'
        self.fields['email'].label = 'E-Mail'
        self.fields['address'].label = '주소'
        self.fields['birthday'].label = '생일'
        self.fields['job'].label = '직업 종류'