from django.db import models
from django.contrib.auth.models import User

class Pessoa(models.Model):
    CPF_Pessoa = models.CharField(max_length=11, default='', null=False)
    FotoPerfil = models.CharField(max_length=50, default='')
    Data_Nascimento = models.DateField()
    Lattes = models.CharField(max_length=80, default='', null=False)
    Status = models.BooleanField(null=False)
    UserName = models.CharField(max_length=100, default='', null=False)

class Professores(models.Model):
    UserName = models.CharField(max_length=100, default='', null=False)
    ID_Professor = models.AutoField(primary_key=True)
    InteressePesquisa = models.CharField(max_length=100, default='', null=False)

class Software(models.Model):
    ID_software = models.AutoField(primary_key=True)
    Titulo = models.CharField(max_length=100, default='', null=False)
    Descricao = models.CharField(max_length=800, default='', null=False)
    Versao = models.CharField(max_length=80, default='', null=False)

class Computadores(models.Model):
    ID_Maquina = models.AutoField(primary_key=True)
    Status_Computador = models.BooleanField(null=False)
    UserName = models.CharField(max_length=100, default='', null=False)

class Alunos(models.Model):
    UserName = models.CharField(max_length=100, default='', null=False)
    ID_Aluno = models.AutoField(primary_key=True)

class Projetos_Pesquisas(models.Model):
    ID_Pesquisa = models.AutoField(primary_key=True)
    Titulo_Pesquisa = models.CharField(max_length=100, default='', null=False)
    Descricao_Pesquisa = models.CharField(max_length=800, default='')
    Area_Pesquisa = models.CharField(max_length=800, default='')

class Professor_Aluno(models.Model):
    ID_Professor = models.ForeignKey(Professores, on_delete=models.CASCADE)
    ID_Aluno = models.ForeignKey(Alunos, on_delete=models.CASCADE)
    models.ForeignKey(Projetos_Pesquisas, on_delete=models.CASCADE)

class Maquina_Software(models.Model):
    ID_Maquina = models.ForeignKey(Computadores, on_delete=models.CASCADE)
    ID_Software = models.ForeignKey(Software, on_delete=models.CASCADE)

class Calendario(models.Model):
    DatasMarcadas = models.DateField()
    Tema = models.CharField(max_length=200, default='', null=False)
    ID_Reuniao = models.AutoField(primary_key=True)

class Calendario_Pessoa(models.Model):
    UserName = models.CharField(max_length=100, default='', null=False)
    ID_Reuniao = models.ForeignKey(Calendario, on_delete=models.CASCADE)

class Inventario(models.Model):
    ID_Objeto = models.AutoField(primary_key=True)
    Nome = models.CharField(max_length=100, default='', null=False)
    Descricao = models.CharField(max_length=200, default='', null=False)
    Status_Objeto = models.BooleanField(null=False)

class Biblioteca(models.Model):
    ID_Artigo = models.AutoField(primary_key=True)
    PDF_Artigo = models.CharField(max_length=100, default='', null=False)
    Titulo = models.CharField(max_length=300, default='', null=False)
    Resumo = models.CharField(max_length=800, default='', null=False)
    Data_Publicao = models.DateField()
    Autor = models.CharField(max_length=100, default='')
    Area_Abordagem = models.CharField(max_length=100, default='', null=False)