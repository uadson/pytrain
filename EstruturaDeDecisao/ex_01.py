'''Faça um Programa que peça dois números e imprima o maior deles.'''

	
num_1 = int(input('1º num.: '))
num_2 = int(input('2º num.: '))


if num_1 > num_2:

	print(num_1)

else:

	print(num_2)

# ou 

print(max(num_1, num_2))