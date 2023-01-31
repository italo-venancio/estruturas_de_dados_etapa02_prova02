class Conjunto:
    def __init__(self):
        self.__tabela = []

        for _ in range(0, 26):
            self.__tabela.append([])

        self.__tamanho = 0

    # recebe uma palavra e retorna um codigo unico
    def calcular_codigo_espalhamento(self, item):
        codigo = 1

        for i in range(0, len(item)):
            codigo = 42*codigo + ord(item[i])

        return codigo

    # recebe o codigo unico e retorna o indice do item na tabela
    def calcula_indice_da_tabela(self, item):
        codigo_espalhamento = self.calcular_codigo_espalhamento(item)
        codigo_espalhamento = abs(codigo_espalhamento)
        return codigo_espalhamento % len(self.__tabela)

    def verificar_carga(self):
        capacidade = len(self.__tabela)
        carga = self.tamanho() / capacidade

        if carga > 0.75:
            self.redimensionar_tabela(capacidade*2)
        elif carga < 0.25:
            self.redimensionar_tabela(max(capacidade/2, 10))

    def redimensionar_tabela(self, nova_capacidade):
        itens = self.pega_todos()
        self.__tabela = []

        for _ in range(0, int(nova_capacidade)):
            self.__tabela.append([])
            self.__tamanho = 0

        for item in itens:
            self.adiciona(item)

    def adiciona(self, item):
        if not self.contem(item):
            # verificar carga antes da adicao de itens
            self.verificar_carga()

            indice = self.calcula_indice_da_tabela(item)
            lista = self.__tabela[indice]
            lista.append(item)

            self.__tamanho += 1

    def remove(self, item):
        if self.contem(item):
            indice = self.calcula_indice_da_tabela(item)
            lista = self.__tabela[indice]
            lista.remove(item)

            self.__tamanho -= 1
            # verificar carga depois da remocao de itens
            self.verificar_carga()

    def contem(self, item):
        indice = self.calcula_indice_da_tabela(item)
        lista = self.__tabela[indice]

        return item in lista
    
    def pega_todos(self):
        itens = []

        for i in range(0, len(self.__tabela)):
            itens = itens + self.__tabela[i]

        return itens

    def tamanho(self):
        return self.__tamanho
