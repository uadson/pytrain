"""Tamanho de strings. Faça um programa que leia 2 strings e informe o 
conteúdo delas seguido do seu comprimento. Informe também se as duas strings 
possuem o mesmo comprimento e são iguais ou diferentes no conteúdo."""

string_1 = input('Frase 1: ')
string_2 = input('Frase 2: ')

print(f'\nFrase 1: {string_1}')
print(f'Frase 2: {string_2}\n')
print(f'A 1ª string possui {len(string_1)} caracteres.')
print(f'A 2ª string possui {len(string_2)} caracteres.\n')

if string_1 == string_2:
    print('As strings são iguais no conteúdo.')
else:
    print('As strings são diferentes no conteúdo.')