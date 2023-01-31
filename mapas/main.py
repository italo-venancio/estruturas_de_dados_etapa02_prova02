from mapa_espalhamento import MapaEspalhamento
from carro import Carro

def testa_mapa():
    mapa01 = MapaEspalhamento()

    carro01 = Carro('Uno', 'Fiat', 'azul', 2012)
    carro02 = Carro('Corolla', 'Toyota', 'vermelho', 2023)
    carro03 = Carro('Fusca', 'Volkswagen', 'preto', 2003)
    carro04 = Carro('Mustang', 'Ford', 'branco', 1960)
    carro05 = Carro('Cadillac', 'Cadillac', 'azul', 1950)

    mapa01.adiciona('ABC-1234', carro01)
    mapa01.adiciona('BCD-2345', carro02)
    mapa01.adiciona('CDE-3456', carro03)
    mapa01.adiciona('DEF-4567', carro04)
    mapa01.adiciona('EFG-5678', carro05)

    print(mapa01.pega('ABC-1234'))
    print(mapa01.pega('BCD-2345'))
    print(mapa01.tamanho())

    mapa01.remove('ABC-1234')
    print(mapa01.pega('ABC-1234'))
    print(mapa01.tamanho())

if __name__ == '__main__':
    testa_mapa()