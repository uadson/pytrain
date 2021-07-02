"""Classe Retangulo: Crie uma classe que modele um retangulo:

    Atributos: 
    LadoA, LadoB (ou Comprimento e Largura, ou Base e Altura,
    a escolher)
    
    Métodos: Mudar valor dos lados, Retornar valor dos lados, 
    calcular Área e calcular Perímetro;
    
    Crie um programa que utilize esta classe. 
    Ele deve pedir ao usuário que informe as medidas de um local. 
    Depois, deve criar um objeto com as medidas e calcular a 
    quantidade de pisos e de rodapés necessárias para o local."""


class Retangulo:
	"""Representação de um triângulo retângulo"""
	def __init__(self, base=None, altura=None):
		self.base = base
		self.altura = altura

	def retorna_valor(self):
		return f'Base: {self.base} - Altura: {self.altura}'


if __name__ == '__main__':
	retangulo = Retangulo(2, 4)

	for key, value in retangulo.__dict__.items():
		print(key, value)

	print(retangulo.retorna_valor())
	