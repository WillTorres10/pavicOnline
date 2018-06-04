from django.contrib.auth.models import User
from django.http import *
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate
from django.views.generic.base import View
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from .forms import *
from .models import *
from django.contrib.auth.views import login, logout

app_name = 'painel'

def index(request):
    if not request.user.is_authenticated:
        return redirect('painel:acessar')
    else:
        usuarioAtual = request.user
        professores = Professores.objects.filter(UserName = usuarioAtual.username)
        alunos = Alunos.objects.filter(UserName=usuarioAtual.username)
        if alunos:
            return render(request, 'painel/homeAluno.html', {'NomeUser': usuarioAtual.first_name})
        else:
            return render(request, 'painel/homeProfessor.html', {'NomeUser' : usuarioAtual.first_name})
        return render(request, 'painel/base.html', {'FormularioLogin': FormularioLogin, 'NomeUser':usuarioAtual.username})

@csrf_exempt
def acessar(request, *args, **kwargs):
    if request.user.is_authenticated:
        return redirect('painel:home')

    kwargs['extra_context'] = {'next': reverse('painel:acessar'), 'FormularioLogin': FormularioLogin}
    kwargs['template_name'] = 'painel/login.html'
    return login(request, *args, **kwargs)


def sair(request, *args, **kwargs):
    kwargs['next_page'] = reverse('painel:acessar')
    return logout(request, *args, **kwargs)

class CadastroProfessor(View):
    template_name = 'painel/cadastroProfessor.html'

    def get(self, request, *args, **kwargs):
        kwargs['extra_context'] = {'next': reverse('painel:home'), 'FormularioCadastro': FormularioCadastroProfessor}
        kwargs['template_name'] = self.template_name
        return login(request, *args, **kwargs)
        #return render(request, *args, **kwargs))

    @csrf_exempt
    def post(self, request):
        form = FormularioCadastroProfessor(request.POST)
        dados_form = form.data

        usuario_auth = User.objects.create_user(dados_form['username'], dados_form['email'],
                                                dados_form['password'])
        usuario_auth.is_active = True
        usuario_auth.first_name = dados_form['primNome']
        usuario_auth.last_name = dados_form['sobreNome']
        usuario_auth.save()

        u = Pessoa(CPF_Pessoa=dados_form['CPF_Pessoa'],
                   Data_Nascimento=dados_form['data_nascimento'],
                   Lattes=dados_form['Lattes'],
                   UserName=usuario_auth.username,
                   Status = True
                )
        u.save()

        prof = Professores(
            UserName = usuario_auth.username,
            InteressePesquisa = dados_form['AreaInteresse'],
        )

        prof.save()
        return render(request, self.template_name)

class CadastroAluno(View):
    template_name = 'painel/cadastroAluno.html'

    def get(self, request, *args, **kwargs):
        kwargs['extra_context'] = {'next': reverse('painel:home'), 'FormularioCadastro': FormularioCadastroAluno}
        kwargs['template_name'] = self.template_name
        return login(request, *args, **kwargs)
        #return render(request, *args, **kwargs))

    @csrf_exempt
    def post(self, request):
        form = FormularioCadastroAluno(request.POST)
        dados_form = form.data

        usuario_auth = User.objects.create_user(dados_form['username'], dados_form['email'], dados_form['password'])
        usuario_auth.is_active = True
        usuario_auth.first_name = dados_form['primNome']
        usuario_auth.last_name = dados_form['sobreNome']
        usuario_auth.save()

        u = Pessoa(CPF_Pessoa=dados_form['CPF_Pessoa'],
                   Data_Nascimento=dados_form['data_nascimento'],
                   Lattes=dados_form['Lattes'],
                   UserName=usuario_auth.username,
                   Status = True
                )
        u.save()

        alu = Alunos(
            UserName=u.UserName
        )
        alu.save()
        return render(request, self.template_name)

def listarUsuarios(request, *args, **kwargs):
    if not request.user.is_authenticated:
        return redirect('painel:acessar')
    else:
        alunos = Alunos.objects.all()
        pessoas = Pessoa.objects.all()
        usuarios = User.objects.all()
        templateName = 'painel/menuProfessor.html'
        if alunos.filter(UserName = request.user.username):
            templateName = 'painel/menuAluno.html'
        atributos = list()
        for user in usuarios:
            pessoa = Pessoa.objects.filter(UserName=user.username)
            pessoaLista = list(pessoa)
            tipo = "Professor"
            if Alunos.objects.filter(UserName=user.username):
                tipo = "Aluno"
            att = list()
            att.append(user.id)
            att.append(user.username)
            att.append(user.first_name + " " + user.last_name)
            att.append(user.email)
            att.append(tipo)
            if pessoa.values('Status'):
                att.append("Ativo")
            else:
                att.append("Desativo")
            atributos.append(att)
        return render(request, 'painel/listarUsuarios.html', {'template':templateName, 'atributos':atributos})
