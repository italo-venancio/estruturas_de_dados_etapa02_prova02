from grafo import GrafoMatriz

def testa_grafo():
    grafo01 = GrafoMatriz(5)
    grafo01.adicionar_aresta(1,3)
    grafo01.adicionar_aresta(1,2)
    grafo01.adicionar_aresta(2,2)
    grafo01.adicionar_aresta(4,5)

    grafo01.imprime_grafo()
    print(grafo01.tem_ligacao(3,1)) 

    grafo01.remover_aresta(1,3)

    grafo01.imprime_grafo()
    print(grafo01.tem_ligacao(3,5)) 

if __name__ == '__main__':
    testa_grafo()