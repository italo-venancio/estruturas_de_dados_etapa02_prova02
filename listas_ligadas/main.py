from listaLigada import ListaLigada

def testa_lista():
    lista01 = ListaLigada()
    lista01.adicionar_comeco('Gil')
    lista01.adicionar_comeco('Sonia')
    lista01.adicionar_comeco('Will')
    lista01.adicionar_comeco('Zac')
    lista01.adicionar_comeco('Aline')
    lista01.adicionar_posicao('Tom', 3)
    lista01.adicionar_comeco('Zac')

    lista01.adicionar_fim('Leo')
    lista01.adicionar_fim('Zac')
    print(lista01)
    print(lista01.tamanho())

    print(lista01.pegar(4))

    print(lista01.contem('Will'))
    print(lista01.contem('Olga'))

    #lista01.remover_comeco()
    #lista01.remover_posicao(2)
    #lista01.remover_fim()
    #lista01.remover_elemento('Gil')
    lista01.remover_todos_elementos('Zac')

    print(lista01)
    print(lista01.tamanho())

if __name__ == '__main__':
    testa_lista()