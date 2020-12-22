'''Faça um programa que peça uma nota, entre zero e dez. Mostre uma mensagem
caso o valor seja inválido e continue pedindo até que o usuário informe um 
valor válido.'''


from random import randint
from time import sleep

while True:
        
    print('Informe uma nota de 0 a 10: \n')
    num = randint(1, 50)

    if num > 10:
        sleep(2)
        print(f'Nota informada: {num}\n')
        print('Nota informada incorretamente!\n')
        
    else:
        sleep(2)
        print(f'Nota informada: {num}')
        break     