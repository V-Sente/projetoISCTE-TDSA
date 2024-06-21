class Criador:
    def __init__(self, username, email_organizacao, data_nascimento, organizacao, cargo):
        self.__username = username
        self.email_organizacao = email_organizacao
        self.__data_nascimento = data_nascimento
        self.organizacao = organizacao
        self.__cargo = cargo

    @property
    def username(self):
        return self.__username

    @username.setter
    def username(self, username):
        self.__username = username

    @property
    def email_organizacao(self):
        return self.__email_organizacao

    @email_organizacao.setter
    def email_organizacao(self, email_organizacao):
        self.__email_organizacao = email_organizacao

    @property
    def data_nascimento(self):
        return self.__data_nascimento

    @data_nascimento.setter
    def data_nascimento(self, data_nascimento):
        self.__data_nascimento = data_nascimento

    @property
    def organizacao(self):
        return self.organizacao

    @organizacao.setter
    def organizacao(self, organizacao):
        self.organizacao = organizacao

    @property
    def cargo(self):
        return self.__cargo

    @cargo.setter
    def cargo(self, cargo):
        self.__cargo = cargo
