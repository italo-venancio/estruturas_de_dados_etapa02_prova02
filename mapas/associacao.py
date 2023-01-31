class Associacao:
    def __init__(self, placa, carro):
        self.__placa = placa
        self.__carro = carro

    @property
    def placa(self):
        return self.__placa

    @placa.setter
    def placa(self, placa):
        self.__placa = placa

    @property
    def carro(self):
        return self.__carro

    @carro.setter
    def carro(self, carro):
        self.__carro = carro
        