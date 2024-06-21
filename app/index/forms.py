# forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser

class CreateUserForm(UserCreationForm):

    class Meta:
        model = CustomUser
        fields = ['username', 'data_nascimento', 'sexo', 'email', 'n_telemovel', 'password1', 'password2']
        widgets = {
            'data_nascimento': forms.DateInput(attrs={'type': 'date'}),
        }

class CreateCreatorForm(UserCreationForm):

    class Meta:
        model = CustomUser
        fields = ['email_organizacao', 'username', 'organizacao', 'cargo']
        widgets = {
            'data_nascimento': forms.DateInput(attrs={'type': 'date'}),
        }
