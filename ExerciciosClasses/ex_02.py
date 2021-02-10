'''Crie uma classe que modele um quadrado:'''


class Quadrado:

	def __init__(self, lado=None, area=None):
		self.lado = lado

	def altera_valor(self, valor):
		self.lado = valor
		return self.lado

	def retorna_valor(self):
		return self.lado

	def calcular_area(self):
		self.area = self.lado ** 2
		return self.area

if __name__ == '__main__':

	q = Quadrado(lado = 4)

	print(f'Lado = {q.lado}')

	q.altera_valor(6)

	print(f'(Novo Valor) Lado = {q.retorna_valor()}')

	print(f'Área = {q.calcular_area()}')