from django.urls import path
from django.contrib.auth import views as auth_views
from django.contrib.auth import views
from django.contrib.auth.decorators import login_required
from . import views
from .views import *


app_name = 'home'

urlpatterns = [
    path('', views.index, name='home')
]