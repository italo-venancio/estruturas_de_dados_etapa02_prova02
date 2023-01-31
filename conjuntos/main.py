from conjunto import Conjunto

def testa_conjunto():
    conj = Conjunto()
    conj.adiciona('It')
    conj.adiciona('Fer')
    conj.adiciona('Joe')
    conj.adiciona('Zac')
    conj.adiciona('Tom')
    conj.adiciona('Gil')
    
    print(conj.pega_todos())

    print(conj.tamanho())

    conj.remove('Zac')
    print(conj.pega_todos())

if __name__ == '__main__':
    testa_conjunto()