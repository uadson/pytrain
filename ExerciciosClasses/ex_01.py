'''Classe Bola: Crie uma classe que modele uma bola:

Atributos: Cor, circunferência, material
Métodos: trocaCor e mostraCor
'''

class Bola:

    def __init__(self, cor=None, circ=None, material=None):

        self.cor = cor
        self.circ = circ
        self.material = material

    def mostra_cor(self):
        return self.cor

    def troca_cor(self, nova_cor):
        nova_cor = 'Azul'
        self.cor = nova_cor
        return self.cor

if __name__ == '__main__':
    print('Bola:')

    bola = Bola('Branca', 15.5, 'Couro')
    print()

    bola.mostra_cor()
    print()

    bola.troca_cor('Azul')
    print()

    bola.mostra_cor()