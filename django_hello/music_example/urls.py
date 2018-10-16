from django.urls import path
from . import views

urlpatterns = [
    path('list/', views.music_list, name='music_list'),
    path('create/', views.music_create, name="music_create")
]