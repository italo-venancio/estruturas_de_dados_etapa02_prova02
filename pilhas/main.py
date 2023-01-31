from pilha import Pilha

def testa_pilha():
    pilha01 = Pilha()
    
    print(pilha01.vazia())

    pilha01.inserir('Suporte')
    pilha01.inserir('Haste')
    pilha01.inserir('Parafuso')
    pilha01.inserir('Canopla')
    pilha01.inserir('Copinho')
    pilha01.inserir('Motor')
    pilha01.inserir('Pas')
    pilha01.inserir('Parafuso')
    pilha01.inserir('Base do Lustre')
    pilha01.inserir('Lustre')
    print(pilha01)
    
    print(pilha01.tamanho())

    pilha01.remover()
    print(pilha01)

if __name__ == '__main__':
    testa_pilha()
