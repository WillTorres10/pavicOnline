from django import forms


class FormularioLogin(forms.Form):
    username = forms.CharField(required=True, label='',
                               widget=forms.TextInput(attrs={'placeholder': 'Usuário', 'class': 'form-control'}))
    password = forms.CharField(required=True, label='',
                               widget=forms.PasswordInput(attrs={'placeholder': 'Senha', 'class': 'form-control'}))


class FormularioCadastroProfessor(forms.Form):
    primNome = forms.CharField(required=True, label='',
                               widget=forms.TextInput(attrs={'placeholder': 'Primeiro Nome', 'class': 'form-control'}))
    sobreNome = forms.CharField(required=True, label='',
                                widget=forms.TextInput(attrs={'placeholder': 'Sobrenome', 'class': 'form-control'}))
    username = forms.CharField(required=True, label='',
                               widget=forms.TextInput(attrs={'placeholder': 'Usuário', 'class': 'form-control'}))
    password = forms.CharField(required=True, label='',
                               widget=forms.PasswordInput(attrs={'placeholder': 'Senha', 'class': 'form-control'}))
    repeatPassword = forms.CharField(required=True, label='',
                                     widget=forms.PasswordInput(
                                         attrs={'placeholder': 'Repetir Senha', 'class': 'form-control'}))
    email = forms.CharField(required=True, label='',
                            widget=forms.TextInput(attrs={'placeholder': 'Email', 'class': 'form-control'}))
    data_nascimento = forms.DateField(label='', widget=forms.DateInput(
        attrs={'placeholder': 'Data de Nascimento', 'class': 'form-control', 'type': "date"}))
    CPF_Pessoa = forms.CharField(required=True, label='',
                                 widget=forms.TextInput(attrs={'placeholder': 'CPF', 'class': 'form-control'}))
    Lattes = forms.URLField(required=True, label='',
                            widget=forms.TextInput(attrs={'placeholder': 'Link Lattes', 'class': 'form-control'}))
    AreaInteresse = forms.CharField(required=True, label='',
                                    widget=forms.TextInput(
                                        attrs={'placeholder': 'Area de pesquisa', 'class': 'form-control'}))


class FormularioCadastroAluno(forms.Form):
    primNome = forms.CharField(required=True, label='',
                               widget=forms.TextInput(attrs={'placeholder': 'Primeiro Nome', 'class': 'form-control'}))
    sobreNome = forms.CharField(required=True, label='',
                                widget=forms.TextInput(attrs={'placeholder': 'Sobrenome', 'class': 'form-control'}))
    username = forms.CharField(required=True, label='',
                               widget=forms.TextInput(attrs={'placeholder': 'Usuário', 'class': 'form-control'}))
    password = forms.CharField(required=True, label='',
                               widget=forms.PasswordInput(attrs={'placeholder': 'Senha', 'class': 'form-control'}))
    repeatPassword = forms.CharField(required=True, label='',
                                     widget=forms.PasswordInput(
                                         attrs={'placeholder': 'Repetir Senha', 'class': 'form-control'}))
    email = forms.CharField(required=True, label='',
                            widget=forms.TextInput(
                                attrs={'placeholder': 'Email', 'class': 'form-control', 'type': 'email'}))
    data_nascimento = forms.DateField(label='', widget=forms.DateInput(
        attrs={'placeholder': 'Data de Nascimento', 'class': 'form-control', 'type': "date"}))
    CPF_Pessoa = forms.CharField(required=True, label='',
                                 widget=forms.TextInput(attrs={'placeholder': 'CPF', 'class': 'form-control'}))
    Lattes = forms.URLField(required=True, label='',
                            widget=forms.TextInput(attrs={'placeholder': 'Link Lattes', 'class': 'form-control'}))
    AreaInteresse = forms.CharField(required=True, label='',
                                    widget=forms.TextInput(
                                        attrs={'placeholder': 'Area de pesquisa', 'class': 'form-control'}))


class FormularioCadastroComputadores(forms.Form):
    status_Computador = forms.BooleanField(required=True, label='', widget=forms.CheckboxInput(
        attrs={'class': 'required checkbox form-control'}))
    username = forms.CharField(required=True, label='',
                               widget=forms.TextInput(attrs={'placeholder': 'Usuário', 'class': 'form-control'}))


class FormularioCadastroSoftware(forms.Form):
    titulo = forms.CharField(required=True, label='',
                             widget=forms.TextInput(attrs={'placeholder': 'Nome do Software', 'class': 'form-control'}))
    descricao = forms.CharField(required=True, label='',
                                widget=forms.TextInput(attrs={'placeholder': 'Descrição', 'class': 'form-control'}))
    versao = forms.CharField(required=True, label='',
                             widget=forms.TextInput(attrs={'placeholder': 'Versão', 'class': 'form-control'}))


class FormularioCadastroCalendario(forms.Form):
    datasMarcadas = forms.DateField(required=True, label='', widget=forms.DateInput(attrs={'type': 'date'}))
    tema = forms.CharField(required=True, label='',
                           widget=forms.TextInput(attrs={'placeholder': 'Tema', 'class': 'form-control'}))


class FormularioCadastroInventario(forms.Form):
    nomeObjeto = forms.CharField(required=True, label='',
                                 widget=forms.TextInput(attrs={'placeholder': 'Nome Objeto', 'class': 'form-control'}))
    descricao = forms.CharField(required=True, label='',
                                widget=forms.TextInput(attrs={'placeholder': 'Descrição', 'class': 'form-control'}))
    status_Objeto = forms.BooleanField(required=True, label='',
                                       widget=forms.CheckboxInput(attrs={'class': 'required checkbox form-control'}))


class FormularioCadastroBiblioteca(forms.Form):
    # pdfArtigo = forms..FileField(upload_to=user_directory_path)
    titulo = forms.CharField(required=True, label='',
                             widget=forms.TextInput(attrs={'placeholder': 'Nome do Artigo', 'class': 'form-control'}))
    resumo = forms.CharField(required=True, label='',
                             widget=forms.TextInput(attrs={'placeholder': 'Resumo', 'class': 'form-control'}))
    dataPublicacao = forms.DateField(required=True, label='', widget=forms.DateInput(attrs={'type': 'date'}))
    autor = forms.CharField(required=True, label='',
                            widget=forms.TextInput(attrs={'placeholder': 'Autor', 'class': 'form-control'}))
    areaAbordagem = forms.CharField(required=True, label='', widget=forms.TextInput(
        attrs={'placeholder': 'Area de Abordagem', 'class': 'form-control'}))