from django.shortcuts import render, redirect
from django.views.generic.base import View
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from .forms import *
from .models import *
from django.contrib.auth.views import login, logout

app_name = 'painel'

def index(request):
    usuarioAtual = request.user
    pessoa = Pessoa.objects.filter(UserName = usuarioAtual.username)
    Nome_completo = usuarioAtual.first_name + " " + usuarioAtual.last_name
    fotoPerfil = str(pessoa.values("FotoPerfil"))
    fotoPerfil = fotoPerfil.replace("<QuerySet [{'FotoPerfil': '", "/media/")
    fotoPerfil = fotoPerfil.replace("'}]>", "")
    alunos = Alunos.objects.filter(UserName=usuarioAtual.username)
    if alunos:
        return render(request, 'painel/homeAluno.html', {'fotoPerfil':fotoPerfil, "nomePessoa":Nome_completo})
    else:
        return render(request, 'painel/homeProfessor.html', {'fotoPerfil':fotoPerfil})
    return render(request, 'painel/base.html', {'FormularioLogin': FormularioLogin, 'fotoPerfil':fotoPerfil})

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
    alunos = Alunos.objects.all()
    usuarios = User.objects.all()
    computadores = Computadores.objects.all()
    templateName = 'painel/menuProfessor.html'

    def get(self, request, *args, **kwargs):
        if self.alunos.filter(UserName=request.user.username):
            return redirect('painel:home')
        kwargs['extra_context'] = {'next': reverse('painel:home'), 'FormularioCadastro': FormularioCadastroProfessor,
                                   'template':self.templateName}
        kwargs['template_name'] = 'painel/cadastroProfessor.html'
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
                   Status = True,
                   FotoPerfil=request.FILES['my_uploaded_file']
                )
        u.save()

        prof = Professores(
            UserName = usuario_auth.username,
            InteressePesquisa = dados_form['AreaInteresse'],
        )

        prof.save()
        return render(request, 'painel/cadastroProfessor.html',{'template':self.templateName})

class CadastroAluno(View):
    alunos = Alunos.objects.all()
    usuarios = User.objects.all()
    computadores = Computadores.objects.all()
    templateName = 'painel/menuProfessor.html'

    def get(self, request, *args, **kwargs):
        if self.alunos.filter(UserName=request.user.username):
            return redirect('painel:home')
        kwargs['extra_context'] = {'next': reverse('painel:home'), 'FormularioCadastro': FormularioCadastroAluno,
                                   'template':self.templateName}
        kwargs['template_name'] = 'painel/cadastroAluno.html'
        return login(request, *args, **kwargs)

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
                   Status=True,
                   FotoPerfil=request.FILES['my_uploaded_file']
                )
        u.save()

        alu = Alunos(
            UserName=u.UserName
        )
        alu.save()
        return render(request, 'painel/cadastroAluno.html',{'template':self.templateName})

class CadastroComputador(View):
    alunos = Alunos.objects.all()
    usuarios = User.objects.all()
    computadores = Computadores.objects.all()
    templateName = 'painel/menuProfessor.html'

    def get(self, request, *args, **kwargs):
        if self.alunos.filter(UserName=request.user.username):
            self.templateName = 'painel/menuAluno.html'
        kwargs['extra_context'] = {'next': reverse('painel:home'), 'FormularioCadastro': FormularioCadastroComputadores,
                                   'usuarios':self.usuarios, 'template':self.templateName}
        kwargs['template_name'] = "painel/cadastroComputador.html"
        return login(request, *args, **kwargs)
        #return render(request, *args, **kwargs))

    @csrf_exempt
    def post(self, request):
        form = FormularioCadastroComputadores(request.POST)
        dados_form = form.data
        computador_novo = Computadores(
            Status_Computador=request.POST['Uso'],
            UserName=request.POST.get('usuariosDono')
        )

        computador_novo.save()
        return render(request, "painel/cadastroComputador.html",{'template':self.templateName})

class CadastroSoftware(View):
    alunos = Alunos.objects.all()
    usuarios = User.objects.all()
    computadores = Computadores.objects.all()
    templateName = 'painel/menuProfessor.html'

    def get(self, request, *args, **kwargs):
        usuarios = User.objects.all()
        if self.alunos.filter(UserName=request.user.username):
            self.templateName = 'painel/menuAluno.html'
        kwargs['extra_context'] = {'next': reverse('painel:home'), 'FormularioCadastro': FormularioCadastroSoftware,
                                   'usuarios':usuarios, 'template':self.templateName}
        kwargs['template_name'] = "painel/cadastroSoftware.html"
        return login(request, *args, **kwargs)

    @csrf_exempt
    def post(self, request):
        form = FormularioCadastroSoftware(request.POST)
        dados_form = form.data

        softwareNovo = Software(
            Titulo=dados_form['titulo'],
            Descricao=dados_form['descricao'],
            Versao=dados_form['versao']
        )
        softwareNovo.save()
        return render(request, "painel/cadastroSoftware.html",{'template':self.templateName})

class CadastroBiblioteca(View):
    alunos = Alunos.objects.all()
    usuarios = User.objects.all()
    computadores = Computadores.objects.all()
    templateName = 'painel/menuProfessor.html'

    def get(self, request, *args, **kwargs):
        usuarios = User.objects.all()
        if self.alunos.filter(UserName=request.user.username):
            self.templateName = 'painel/menuAluno.html'
        kwargs['extra_context'] = {'next': reverse('painel:home'), 'FormularioCadastro': FormularioCadastroBiblioteca,
                                   'usuarios': usuarios, 'template': self.templateName}
        kwargs['template_name'] = "painel/cadastroBiblioteca.html"
        return login(request, *args, **kwargs)

    @csrf_exempt
    def post(self, request):
        form = FormularioCadastroSoftware(request.POST, request.FILES)
        dados_form = form.data

        bibliotecaNovo = Biblioteca(
            Titulo=dados_form['titulo'],
            Resumo=dados_form['resumo'],
            Data_Publicao=dados_form['dataPublicacao'],
            Autor=dados_form['autor'],
            Area_Abordagem=dados_form['areaAbordagem'],
            PDF_Arquivo=request.FILES['my_uploaded_file']
        )
        bibliotecaNovo.save()

        return render(request, "painel/cadastroBiblioteca.html", {'template': self.templateName})

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
            plista = list(pessoa)
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
            lattes = str(list(pessoa.values("Lattes"))).replace("[{'Lattes': '","")
            lattes = lattes.replace("'}]","")
            lattesURL = "<a href='"+lattes+"' target='_blank'>Acessar</a>"
            att.append(lattesURL)
            atributos.append(att)
        return render(request, 'painel/listarUsuarios.html', {'template':templateName, 'atributos':atributos})

def listarComputadores(request):
    if not request.user.is_authenticated:
        return redirect('painel:acessar')
    else:
        alunos = Alunos.objects.all()
        usuarios = User.objects.all()
        computadores = Computadores.objects.all()
        templateName = 'painel/menuProfessor.html'
        if alunos.filter(UserName = request.user.username):
            templateName = 'painel/menuAluno.html'
        atributos = list()
        for pc in computadores:
            att = list()
            att.append(pc.ID_Maquina)
            usuario = usuarios.get(username=pc.UserName)
            att.append(usuario.first_name + " " + usuario.last_name)
            if pc.Status_Computador:
                att.append("Em uso")
            else:
                att.append("Sem uso")
            atributos.append(att)
        return render(request, 'painel/listarComputadores.html', {'template':templateName, 'atributos':atributos})

def listarSoftware(request):
    if not request.user.is_authenticated:
        return redirect('painel:acessar')
    else:
        alunos = Alunos.objects.all()
        usuarios = User.objects.all()
        softwares = Software.objects.all()
        templateName = 'painel/menuProfessor.html'
        if alunos.filter(UserName = request.user.username):
            templateName = 'painel/menuAluno.html'
        atributos = list()
        for pc in softwares:
            att = list()
            att.append(pc.ID_software)
            att.append(pc.Titulo)
            att.append(pc.Descricao)
            att.append(pc.Versao)
            atributos.append(att)
        return render(request, 'painel/listarSoftware.html', {'template':templateName, 'atributos':atributos})

def listarBiblioteca(request):
    if not request.user.is_authenticated:
        return redirect('painel:acessar')
    else:
        alunos = Alunos.objects.all()
        biblioteca = Biblioteca.objects.all()
        templateName = 'painel/menuProfessor.html'
        if alunos.filter(UserName = request.user.username):
            templateName = 'painel/menuAluno.html'
        atributos = list()
        for bib in biblioteca:
            att = list()
            att.append(bib.ID_Artigo)
            att.append(bib.Titulo)
            att.append(bib.Resumo)
            att.append(bib.Data_Publicao)
            att.append(bib.Autor)
            att.append(bib.Area_Abordagem)
            URL = "<a href='"+bib.PDF_Arquivo.url+"' target='_blank'>Acessar</a>"
            att.append(URL)
            atributos.append(att)
        return render(request, 'painel/listarBiblioteca.html', {'template':templateName, 'atributos':atributos})