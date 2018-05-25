from django import forms

class FormularioLogin(forms.Form):
    username = forms.CharField(required=True, label='',widget=forms.TextInput(attrs={'placeholder': 'Usuário', 'class': 'form-control'}))
    password = forms.CharField(required=True, label='', widget=forms.PasswordInput(attrs={'placeholder': 'Senha', 'class': 'form-control'}))

class FormularioCadastroProfessor(forms.Form):
    primNome = forms.CharField(required=True, label='', widget=forms.TextInput(attrs={'placeholder': 'Primeiro Nome', 'class': 'form-control'}))
    sobreNome = forms.CharField(required=True, label='', widget=forms.TextInput(attrs={'placeholder': 'Sobrenome', 'class': 'form-control'}))
    username = forms.CharField(required=True, label='', widget=forms.TextInput(attrs={'placeholder': 'Usuário', 'class': 'form-control'}))
    password = forms.CharField(required=True, label='', widget=forms.PasswordInput(attrs={'placeholder': 'Senha', 'class': 'form-control'}))
    repeatPassword = forms.CharField(required=True, label='',
                               widget=forms.PasswordInput(attrs={'placeholder': 'Repetir Senha', 'class': 'form-control'}))
    email = forms.CharField(required=True, label='',
                               widget=forms.TextInput(attrs={'placeholder': 'Email', 'class': 'form-control'}))
    data_nascimento = forms.DateField(label='', widget=forms.DateInput(attrs={'placeholder': 'Data de Nascimento', 'class': 'form-control','type': "date"}))
    CPF_Pessoa = forms.CharField(required=True, label='', widget=forms.TextInput(attrs={'placeholder': 'CPF', 'class': 'form-control'}))
    Lattes = forms.URLField(required=True, label='', widget=forms.TextInput(attrs={'placeholder': 'Link Lattes', 'class': 'form-control'}))
    AreaInteresse = forms.CharField(required=True, label='',
                                 widget=forms.TextInput(attrs={'placeholder': 'Area de pesquisa', 'class': 'form-control'}))

class FormularioCadastroAluno(forms.Form):
    primNome = forms.CharField(required=True, label='', widget=forms.TextInput(attrs={'placeholder': 'Primeiro Nome', 'class': 'form-control'}))
    sobreNome = forms.CharField(required=True, label='', widget=forms.TextInput(attrs={'placeholder': 'Sobrenome', 'class': 'form-control'}))
    username = forms.CharField(required=True, label='', widget=forms.TextInput(attrs={'placeholder': 'Usuário', 'class': 'form-control'}))
    password = forms.CharField(required=True, label='', widget=forms.PasswordInput(attrs={'placeholder': 'Senha', 'class': 'form-control'}))
    repeatPassword = forms.CharField(required=True, label='',
                               widget=forms.PasswordInput(attrs={'placeholder': 'Repetir Senha', 'class': 'form-control'}))
    email = forms.CharField(required=True, label='',
                               widget=forms.TextInput(attrs={'placeholder': 'Email', 'class': 'form-control', 'type':'email'}))
    data_nascimento = forms.DateField(label='', widget=forms.DateInput(attrs={'placeholder': 'Data de Nascimento', 'class': 'form-control','type': "date"}))
    CPF_Pessoa = forms.CharField(required=True, label='', widget=forms.TextInput(attrs={'placeholder': 'CPF', 'class': 'form-control'}))
    Lattes = forms.URLField(required=True, label='', widget=forms.TextInput(attrs={'placeholder': 'Link Lattes', 'class': 'form-control'}))
    AreaInteresse = forms.CharField(required=True, label='',
                                 widget=forms.TextInput(attrs={'placeholder': 'Area de pesquisa', 'class': 'form-control'}))