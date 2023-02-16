from django.urls import path

from . import views

app_name = 'posts'

urlpatterns = [

    path('', views.index, name='posts_main_padge'),
    path('group/<slug:slug>/', views.posts_list),
]
