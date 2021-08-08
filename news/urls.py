from django.urls import path,include
from news import views
urlpatterns = [
    path('', views.newshome, name='newshome' ),
]
