'''
Define uma classe Cliente em Python, com métodos de acesso e modificação (getters e setters) usando propriedades.
Definição da classe Cliente: Cria uma nova classe chamada Cliente.
'''
class Cliente:
    '''
    Método Construtor init    
    Método __init__: É o construtor da classe. Ele é chamado quando uma nova instância da classe é criada. 
    '''
    def __init__(self, nome, sexo, data_nascimento, email, profissao):
        '''
        Parâmetros:
        nome: Nome do cliente.
        sexo: Sexo do cliente.
        data_nascimento: Data de nascimento do cliente.
        email: Endereço de email do cliente.
        profissao: Profissão do cliente.

        Atributos privados:
        self.__nome: Atributo privado para armazenar o nome.
        self.__sexo: Atributo privado para armazenar o sexo.
        self.__data_nascimento: Atributo privado para armazenar a data de nascimento.
        self.__email: Atributo privado para armazenar o email.
        self.__profissao: Atributo privado para armazenar a profissão.   
        '''
        self.__nome = nome
        self.__sexo = sexo
        self.__data_nascimento = data_nascimento
        self.__email = email
        self.__profissao = profissao

    '''
    Propriedades
    Propriedade nome    
    Getter para nome: O decorador @property transforma o método nome em um getter,
    permitindo acessar self.__nome com cliente.nome.
    Setter para nome: O decorador @nome.setter define o método nome como o setter para self.__nome,
    permitindo modificar self.__nome com cliente.nome = novo_nome.
    '''
    @property
    def nome(self):
        return self.__nome
    @nome.setter
    def nome(self, nome):
        self.__nome = nome


    @property
    def sexo(self):
        return self.__sexo
    
    @sexo.setter
    def sexo(self, sexo):
        self.__sexo = sexo


    @property
    def data_nascimento(self):
        return self.__data_nascimento
    
    @data_nascimento.setter
    def data_nascimento(self, data_nascimento):
        self.__data_nascimento = data_nascimento


    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, email):
        self.__email = email


    @property
    def profissao(self):
        return self.__profissao
    
    @profissao.setter
    def profissao(self, profissao):
        self.__profissao = profissao