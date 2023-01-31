class GrafoMatriz:
    def __init__(self, qtd_vertices):
        self.qtd_vertices = qtd_vertices
        self.grafo = [[0] * self.qtd_vertices for _ in range(self.qtd_vertices)]

    def adicionar_aresta(self, a, b):
        self.grafo[a-1][b-1] = 1
        self.grafo[b-1][a-1] = 1

    def remover_aresta(self, a, b):
        self.grafo[a-1][b-1] = 0
        self.grafo[b-1][a-1] = 0

    def imprime_grafo(self):
        for i in self.grafo:
            for j in i:
                print(j, end='  ')
            print('')

    def tem_ligacao(self, a, b):
        if self.grafo[a-1][b-1] == 1:
            return f'{a}, {b}: {True}'
        return f'{a}, {b}: {False}'

