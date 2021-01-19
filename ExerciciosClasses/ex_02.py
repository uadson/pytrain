class Quadrado:

	def __init__(self, lado):
		self.lado = lado

	def altera_valor(self, valor):
		self.lado = valor
		return self.lado

	def retorna_valor(self):
		print(f'Valor do Lado do Quadrado alterado para:{self.lado}')

	def calcular_area(self):
		area = self.lado ** 2
		print(f'A área do Quadrado é: {area}')

if __name__ == '__main__':

	q = Quadrado(4)

	print(f'Valor do Lado do Quadrado: {q.lado}')

	q.altera_valor(6)

	q.retorna_valor()

	q.calcular_area()