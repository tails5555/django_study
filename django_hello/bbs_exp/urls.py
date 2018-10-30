from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='bbs_index'),
    path('list/', views.post_list, name='post_list'),
    path('create/', views.post_create, name='post_create'),
    path('edit/', views.post_update, name='post_update')
]