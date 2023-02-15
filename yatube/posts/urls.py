# ice_cream/urls.py
from django.urls import path
from . import views

app_name = 'posts_1'

urlpatterns = [

    path('', views.index, name='posts_main_padge'),
    path('group/<slug:pk>/', views.posts_list),

    path('justpage/', views.JustStaticPage.as_view()),
    path('profile/<str:username>/', views.profile, name='profile'),
    path('posts/<int:post_id>/', views.post_detail, name='post_detail'),
]
