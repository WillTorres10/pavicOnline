from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from painel.models import *

app_name = 'home'

def index(request):
    Usuarios = User.objects.all()
    Pessoas = Pessoa.objects.all()
    listaUsuarios = list()
    for user in Usuarios:
        novoUser = list()
        pessoa = Pessoa.objects.filter(UserName=user.username)
        lattes = str(list(pessoa.values("Lattes"))).replace("[{'Lattes': '", "")
        lattes = lattes.replace("'}]", "")
        if pessoa.values("FotoPerfil"):
            fotoPerfil = str(pessoa.values("FotoPerfil"))
            fotoPerfil = fotoPerfil.replace("<QuerySet [{'FotoPerfil': '", "/media/")
            fotoPerfil = fotoPerfil.replace("'}]>", "")
        else:
            fotoPerfil = "/static/assets/images/user.svg"

        #Adicioanando dados na lista
        novoUser.append('<img src="'+fotoPerfil+'" style="width:120px; height:120px; margin-bottom:15px;">')
        novoUser.append('<h3><a href="'+lattes+'"target="_blank">'+user.first_name + " " + user.last_name+ '</a></h3>')
        listaUsuarios.append(novoUser)
    return render(request, 'home/index.html', {'atributos':listaUsuarios})