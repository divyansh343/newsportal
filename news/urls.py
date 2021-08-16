from django.urls import path,include
from news.models import Post
from news import views
urlpatterns = [
    path('', views.bloghome, name='bloghome'),
    path('<str:slug>', views.blogpost, name='blogpost'),
]
