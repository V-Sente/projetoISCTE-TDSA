from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .services import user_services, criador_services
from .entidades import usuario, criador
from .models import CustomUser


# Create your views here.
from .forms import CreateUserForm, CreateCreatorForm

def index(request):
    return render(request, 'index.html')


@login_required(login_url='index')
def dashboard(request):
    return render(request, 'dashboard.html')


def cadastrar_usuario(request):
    if request.method == "POST":
        form_usuario = CreateUserForm(request.POST)
        if form_usuario.is_valid():
            form_usuario.save()
            username = form_usuario.cleaned_data['username']
            data_nascimento = form_usuario.cleaned_data['data_nascimento']
            sexo = form_usuario.cleaned_data['sexo']
            email = form_usuario.cleaned_data['email']
            n_telemovel = form_usuario.cleaned_data['n_telemovel']
            usuario_novo = usuario.Usuario(username=username, data_nascimento=data_nascimento, sexo=sexo, email=email, n_telemovel=n_telemovel)
            messages.success(request, f'Conta criada para {username}')
            
            user_services.cadastrar_user(usuario_novo)
            return redirect('index')
    else:
        form_usuario = CreateUserForm()
    return render(request, 'usuarios/form_usuario.html', {"form_usuario": form_usuario})


def cadastrar_criador(request):
    if request.method == "POST":
        form_criador = CreateCreatorForm(request.POST)
        if form_criador.is_valid():
            username = form_criador.cleaned_data['username']
            data_nascimento = form_criador.cleaned_data['data_nascimento']
            email_organizacao = form_criador.cleaned_data['email_organizacao']
            organizacao = form_criador.cleaned_data['organizacao']
            cargo = form_criador.cleaned_data['cargo']
            criador_novo = criador.Criador(username=username, data_nascimento=data_nascimento, email_organizacao=email_organizacao, organizacao=organizacao, cargo=cargo)
            messages.success(request, f'Parabéns {username}, és criador!')
            
            criador_services.cadastrar_criador(criador_novo)
            return redirect('index')    
    else:
        form_criador = CreateCreatorForm()
    return render(request, 'usuarios/form_criador.html', {"form_criador": form_criador})


def logar_usuario(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        usuario = authenticate(request, username=username, password=password)
        if usuario is not None:
            login(request, usuario)
            return redirect('dashboard')
        else:
            messages.error(request, 'As credenciais estão incorretas')
            return redirect('index')
    else:
        form_login = AuthenticationForm()
    return render(request, 'usuarios/login.html', {"form_login": form_login})


def deslogar_usuario(request):
    logout(request)
    return redirect('index')