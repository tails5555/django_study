from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('list/', views.music_list, name='music_list'),
    path('create/', views.music_create, name='music_create'),
    path('edit/', views.music_update, name='music_update'),
    path('delete/', views.music_delete, name='music_delete'),
    path('genre/list/', views.genre_list, name='genre_list'),
    path('genre/create/', views.genre_create, name='genre_create'),
    path('genre/edit/<int:id>', views.genre_update, name='genre_update'),
    path('genre/delete/<int:id>', views.genre_delete, name='genre_delete')
]