'''
Importação do módulo models do Django:
Este módulo contém classes e funções para definir modelos, que são representações de tabelas no banco de dados.
'''
from django.db import models

# Create your models here.
'''
Definição da classe Cliente:
Define uma classe Cliente que herda de models.Model
 Isso indica que Cliente é um modelo Django, e Django irá criar uma tabela correspondente no banco de dados.
'''
class Cliente(models.Model):
    '''
    SEXO_CHOICES: Define uma tupla de tuplas contendo as opções disponíveis para o campo sexo.
    Cada tupla interna contém um valor de banco de dados e uma descrição legível para humanos.    
    '''
    SEXO_CHOICES = (
        ("F", "Feminino"),
        ("M", "Masculino"),
        ("N", "Nenhuma das opções"),
    )

    '''
    nome: Define um campo de texto (CharField) com um comprimento máximo de 100 caracteres.
    null=False indica que este campo não pode ser nulo no banco de dados.
    blank=False indica que este campo não pode ser deixado em branco no formulário.    
    '''
    nome = models.CharField(max_length=100, null=False, blank=False)

    '''
    data_nascimento: Define um campo de data (DateField).
    null=False e blank=False indicam que este campo é obrigatório.    
    '''
    data_nascimento = models.DateField(null=False, blank=False)

    '''
    email: Define um campo de email (EmailField).
    Este campo deve conter um endereço de email válido.
    null=False e blank=False indicam que este campo é obrigatório.    
    '''
    email = models.EmailField(null=False, blank=False)

    '''
    profissao: Define um campo de texto (CharField) com um comprimento máximo de 50 caracteres.
    null=False e blank=False indicam que este campo é obrigatório.    
    '''
    profissao = models.CharField(max_length=50, null=False, blank=False)

    '''
    sexo: Define um campo de texto (CharField) com um comprimento máximo de 1 caractere.
    choices=SEXO_CHOICES restringe os valores permitidos para este campo às opções definidas em SEXO_CHOICES.
    null=False e blank=False indicam que este campo é obrigatório.    
    '''
    sexo = models.CharField(max_length=1, choices=SEXO_CHOICES, blank=False, null=False)

    '''
    Método Especial str    
    __str__: Define o método __str__ para a classe Cliente.
    Esse método retorna o valor do campo nome quando a instância do modelo é convertida para uma string,
    o que é útil para representações legíveis, como no painel de administração do Django.
    '''
    def __str__(self):
        return self.nome
