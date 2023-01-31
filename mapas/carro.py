class Carro:
    def __init__(self, nome, marca, cor, ano):
        self.__nome = nome 
        self.__marca = marca
        self.__cor = cor 
        self.__ano = ano

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    @property
    def marca(self):
        return self.__marca

    @marca.setter
    def marca(self, marca):
        self.__marca = marca

    @property
    def cor(self):
        return self.__cor

    @cor.setter
    def cor(self, cor):
        self.__cor = cor

    @property
    def ano(self):
        return self.__ano

    @ano.setter
    def ano(self, ano):
        self.__ano = ano

    def __str__(self):
        descricao = f"[{self.__nome}, {self.__marca}, {self.__cor}, {self.__ano}]"
        
        return descricao
        