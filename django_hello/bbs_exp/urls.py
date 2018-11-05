from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='bbs_index'),
    path('list/', views.post_list, name='post_list'),
    path('create/', views.post_create, name='post_create'),
    path('edit/<int:id>', views.post_update, name='post_update'),
    path('view/<int:id>', views.post_view, name='post_view'),
    path('delete/<int:id>', views.post_delete, name='post_delete')
]