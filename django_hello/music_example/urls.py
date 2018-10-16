from django.urls import path
from . import views

urlpatterns = [
    path('list/', views.music_list, name='music_list'),
]