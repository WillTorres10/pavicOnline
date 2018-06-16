from django.urls import path
from django.contrib.auth import views as auth_views
from django.contrib.auth import views
from django.contrib.auth.decorators import login_required
from . import views
from .views import *


app_name = 'painel'

urlpatterns = [
    path('', login_required(views.index), name='home'),
    path('acessar/', views.acessar, name='acessar'),
    path('cadastroProfessor/', login_required(CadastroProfessor.as_view()), name='cadastroProfessor'),
    path('cadastroAluno/', login_required(CadastroAluno.as_view()), name='cadastroAluno'),
    path('listarUsuarios/', login_required(views.listarUsuarios), name='listarUsuarios'),
    path('cadastroComputador/', login_required(CadastroComputador.as_view()), name='cadastroComputador'),
    path('listarComputadores/', login_required(views.listarComputadores), name='listarComputadores'),
    path('cadastroSoftware/', login_required(CadastroSoftware.as_view()), name='cadastroSoftware'),
    path('listarSoftwares/', login_required(views.listarSoftware), name='listarSoftwares'),
    path('alterarSoftware/', login_required(AlterarSoftware.as_view()), name='alterarSoftware'),
    path('cadastroBiblioteca/', login_required(CadastroBiblioteca.as_view()), name='cadastroBiblioteca'),
    path('listarBiblioteca/', login_required(views.listarBiblioteca), name='listarBiblioteca'),
    path('alterarComputador/', login_required(AlterarComputador.as_view()), name='alterarComputador'),
    path('removerComputador/', login_required(RemoverComputador.as_view()), name='removerComputador'),
    path('sair/', views.sair, name='sair'),
]