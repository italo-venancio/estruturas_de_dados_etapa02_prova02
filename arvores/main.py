from arvore_binaria_busca import ArvoreBinariaBusca

def testa_arvore():
    arvore01 = ArvoreBinariaBusca()
    arvore01.inserir(10)
    arvore01.inserir(5)
    arvore01.inserir(15)
    arvore01.inserir(4)
    arvore01.inserir(12)
    arvore01.inserir(13)
    arvore01.inserir(20)
    arvore01.inserir(19)
    arvore01.inserir(25)
    
    arvore01.imprimir_pre(arvore01.raiz)

    arvore01.remover(15)
    print('removido.')

    arvore01.imprimir_pre(arvore01.raiz)


if __name__ == '__main__':
    testa_arvore()