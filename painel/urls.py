from django.urls import path
from django.contrib.auth import views as auth_views
from django.contrib.auth import views
from . import views
from .views import *

app_name = 'painel'

urlpatterns = [
    path('', views.index, name='home'),
    path('acessar/', views.acessar, name='acessar'),
    path('cadastroProfessor/', CadastroProfessor.as_view(), name='cadastroProfessor'),
    path('cadastroAluno/', CadastroAluno.as_view(), name='cadastroAluno'),
    path('sair/', views.sair, name='sair'),
]