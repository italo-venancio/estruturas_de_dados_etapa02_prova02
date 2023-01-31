class No:
    def __init__(self, label):
        self.__esquerda = None
        self.__direita = None
        self.__label = label

    @property
    def esquerda(self):
        return self.__esquerda

    @esquerda.setter
    def esquerda(self, esquerda):
        self.__esquerda = esquerda

    @property
    def direita(self):
        return self.__direita

    @direita.setter
    def direita(self, direita):
        self.__direita = direita

    @property
    def label(self):
        return self.__label

    @label.setter
    def label(self, label):
        self.__label = label
