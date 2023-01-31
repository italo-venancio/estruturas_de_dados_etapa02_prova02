import sys
sys.path.append('..')

from listas_ligadas.celula import Celula
from listas_ligadas.listaLigada import ListaLigada

class Fila:
    def __init__(self):
        self.__itens = ListaLigada()

    def inserir(self, item):
        self.__itens.adicionar_fim(item)

    def remover(self):
        self.__itens.remover_comeco()

    def vazia(self):
        if self.__itens.tamanho() == 0:
            return True
        return False
    
    def tamanho(self):
        return self.__itens.tamanho()

    def __str__(self):
        return self.__itens.__str__()

    