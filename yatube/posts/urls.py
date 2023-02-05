# ice_cream/urls.py
from django.urls import path
from . import views

app_name = 'posts_1'

urlpatterns = [
    
    path('', views.index, name='posts_main_padge'),
    
    path('group_list/', views.posts_list, name='posts_second_padge'),
    path('group_list/<slug:pk>/', views.posts_list),
]