from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required


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
            return redirect('index')
    else:
        form_usuario = CreateUserForm()
    return render(request, 'usuarios/form_usuario.html', {"form_usuario": form_usuario})


def cadastrar_criador(request):
    if request.method == "POST":
        form_criador = CreateCreatorForm(request.POST)
        if form_criador.is_valid():
            form_criador.save()
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