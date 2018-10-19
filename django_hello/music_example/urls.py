from django.urls import path
from . import views

urlpatterns = [
    path('list/', views.music_list, name='music_list'),
    path('create/', views.music_create, name='music_create'),
    path('edit/', views.music_update, name='music_update'),
    path('delete/', views.music_delete, name='music_delete')
]