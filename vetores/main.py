from vetor import Vetor

def testa_vetor():
    vetor01 = Vetor()
    vetor01.adicionar('Zac')
    vetor01.adicionar('Vivi')
    vetor01.adicionar('Lu')
    vetor01.adicionar('Beto')
    vetor01.adicionar('Joe')
    vetor01.adicionar('It')
    
    vetor01.adicionar_posicao('Nick', 2)
    vetor01.adicionar('Joe')
    vetor01.adicionar_posicao('Joe', 0)
    print(vetor01)
    print(vetor01.tamanho())
    
    print(vetor01.pegar(4))

    print(vetor01.contem('Tom'))
    print(vetor01.contem('Zac'))

    #vetor01.remover()
    #vetor01.remover_posicao(4)
    #vetor01.remover_elemento('Lu')
    vetor01.remover_todos_elementos('Joe')
    print(vetor01)

if __name__ == '__main__':
    testa_vetor()