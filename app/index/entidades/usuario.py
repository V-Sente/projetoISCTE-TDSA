class Usuario:
    def __init__(self, username, sexo, data_nascimento, email, n_telemovel):
        self.__username = username
        self.__sexo = sexo
        self.__data_nascimento = data_nascimento
        self.__email = email
        self.__n_telemovel = n_telemovel

    @property
    def username(self):
        return self.__username

    @username.setter
    def username(self, username):
        self.__username = username

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
    def n_telemovel(self):
        return self.__n_telemovel

    @n_telemovel.setter
    def n_telemovel(self, n_telemovel):
        self.__n_telemovel = n_telemovel
