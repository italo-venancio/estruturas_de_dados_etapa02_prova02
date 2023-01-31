from associacao import Associacao

class MapaEspalhamento:
    def __init__(self):
        self.__tabela = []

        for _ in range(0, 30):
            self.__tabela.append([])

        self.__tamanho = 0

    # retorna o codigo unico
    def funcao_hash(self, placa):
        codigo = 1
        
        for i in range(0, len(placa)):
            codigo = 7*codigo + ord(placa[i])
        return codigo

    # retorna o indice correspondente ao codigo
    def calcula_indice_tabela(self, placa):
        codigo_espalhamento = self.funcao_hash(placa)
        codigo_espalhamento = abs(codigo_espalhamento)
        return codigo_espalhamento % len(self.__tabela)

    # verifica se o mapa contem a placa 
    def contem_chave(self, placa):
        indice = self.calcula_indice_tabela(placa)
        lista = self.__tabela[indice]

        for associacao in lista:
            if placa == associacao._Associacao__placa:
                return True
        return False

    def adiciona(self, placa, carro):
        if self.contem_chave(placa):
            self.remove(placa)
        
        indice = self.calcula_indice_tabela(placa)
        lista = self.__tabela[indice]

        associacao = Associacao(placa, carro)
        lista.append(associacao)

        self.__tamanho += 1

    def remove(self, placa):
        if self.contem_chave(placa):
            indice = self.calcula_indice_tabela(placa)
            lista = self.__tabela[indice]

            for associacao in lista:
                if placa == associacao._Associacao__placa:
                    lista.remove(associacao)

            self.__tamanho -= 1

    # recebe uma placa e retorna o carro correspondente
    def pega(self, placa):
        indice = self.calcula_indice_tabela(placa)
        lista = self.__tabela[indice]

        for associacao in lista:
            if placa == associacao._Associacao__placa:
                return str(associacao._Associacao__carro)
        return False

    def tamanho(self):
        return self.__tamanho