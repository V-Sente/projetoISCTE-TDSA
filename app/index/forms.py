from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User


class CreateUserForm(UserCreationForm):
    nome = forms.CharField(widget=forms.Textarea())  # ALTERANDO O TAMANHO DA CAIXA DE TEXTO

    class Meta:
        model = User
        fields = ['nome', 'email', 'data_nascimento', 'sexo', 'n_telemovel', 'password1', 'password2']
        widgets = {
            'data_nascimento': forms.DateInput(attrs={'type': 'date'}),
        }


class CreateCreatorForm(UserCreationForm):
    nome = forms.CharField(widget=forms.Textarea())  # ALTERANDO O TAMANHO DA CAIXA DE TEXTO

    class Meta:
        model = User
        fields = ['nome', 'email', 'data_nascimento', 'sexo', 'n_telemovel', 'organizacao', 'cargo', 'password1', 'password2']
        widgets = {
            'data_nascimento': forms.DateInput(attrs={'type': 'date'}),
        }