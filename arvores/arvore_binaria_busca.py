from no import No

class ArvoreBinariaBusca:
    def __init__(self):
        self.__raiz = None

    def inserir(self, valor):
        novo_no = No(valor)
        
        if self.vazia() == True:
            self.__raiz = novo_no
        else:
            no_pai = None
            no_atual = self.__raiz
            while True:
                if no_atual is not None:
                    no_pai = no_atual
                    if novo_no.label < no_atual.label:
                        no_atual = no_atual.esquerda
                    else:
                        no_atual = no_atual.direita
                else:
                    if novo_no.label < no_pai.label:
                        no_pai.esquerda = novo_no
                    else:
                        no_pai.direita = novo_no
                    break

    def vazia(self):
        if self.__raiz is None:
            return True
        else:
            return False

    @property 
    def raiz(self):
        return self.__raiz

    def imprimir_pre(self, no_atual):
        if no_atual is not None:
            print(no_atual.label)
            self.imprimir_pre(no_atual.esquerda)
            self.imprimir_pre(no_atual.direita)

    def imprimir_pos(self, no_atual):
        if no_atual is not None:
            self.imprimir_pre(no_atual.esquerda)
            self.imprimir_pre(no_atual.direita)
            print(no_atual.label)

    def imprimir_intra(self, no_atual):
        if no_atual is not None:
            self.imprimir_pre(no_atual.esquerda)
            print(no_atual.label)
            self.imprimir_pre(no_atual.direita)

    # o parametro opcional no sera usado para recursao
    def remover(self, valor, no=None):
        if no==None:
            raiz = self.raiz
        else:
            raiz = no

        if raiz == None:
            return raiz
        elif valor < raiz.label:
            raiz.esquerda = self.remover(valor, raiz.esquerda)
        elif valor > raiz.label:
            raiz.direita = self.remover(valor, raiz.direita)
        # o no foi encontrado    
        else: 
            # caso 1: no-folha
            if raiz.esquerda == None and raiz.direita == None:
                raiz = None
            # caso 2: um filho
            elif raiz.esquerda == None:
                no_pai = raiz
                raiz = raiz.direita
                no_pai = None
            elif raiz.direita == None:
                no_pai = raiz
                raiz = raiz.esquerda
                no_pai = None
            # caso 3: dois filhos
            else: 
                no_pai = self.encontra_minimo(raiz.direita)
                raiz.label = no_pai.label
                raiz.direita = self.remover(no_pai.label, raiz.direita)
        return raiz

    def encontra_minimo(self, no):
        no_atual = no

        while no_atual.esquerda != None:
            no_atual = no_atual.esquerda
        
        return no_atual


