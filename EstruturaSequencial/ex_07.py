"""Faça um Programa que calcule a área de um quadrado, 
em seguida mostre o dobro desta área para o usuário. """

# Um quadrado possue lados iguais;
# Logo Área = Lado² ou Área = Lado x Lado


print('Informe o valor dos lados do quadrado:\n')

lado = int(input('Valor: '))

area = lado ** 2

dobro_area = area ** 2

print(f'A área do quadrado é: {area} e dobro desta área é: {dobro_area}\n')

print('=' * 50)

