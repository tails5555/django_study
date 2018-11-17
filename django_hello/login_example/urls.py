from django.urls import path
from . import views

urlpatterns = [
    path('guest/sign', views.sign_up, name='guest_sign_up')
]