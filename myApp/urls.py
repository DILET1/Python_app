from django.urls import path
from . import views

# '' path represents the root of the app
urlpatterns = [
    path('', views.index, name='index'),
]