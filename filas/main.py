from fila import Fila

def testa_fila():
    fila01 = Fila()

    fila01.inserir('Fer')
    fila01.inserir('Leo')
    fila01.inserir('Zac')
    fila01.inserir('Tom')
    fila01.inserir('Joe')
    fila01.inserir('Will')
    print(fila01)

    print(fila01.tamanho())

    fila01.remover()
    print(fila01)
    print(fila01.vazia())
    
if __name__ == '__main__':
    testa_fila()