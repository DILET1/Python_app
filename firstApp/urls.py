from django.urls import path
from . import views

# '' path represents the root of the app
urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('form/', views.form, name='form'),
    path('kewlwebsites/', views.kewlWebsites, name='kewlwebsites'),
    path('greet/', views.greet, name='greet'),
    path('login/', views.login, name="login")
]
