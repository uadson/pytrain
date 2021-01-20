def convert_number(value):
    # função que irá converter um número
    try:
        # 1º tenta converter para um tipo inteiro
        value = int(value)
        # Se bem sucedido retorna o valor convertido
        return value
    # se não:
    except ValueError:
        try:
            # 2º tenta converter para tipo flutuante
            value = float(value)
            # se bem sucedido retorna o valor convertido
            return value
        except ValueError:
            pass
        
while True:
    value = convert_number(input('Enter a number: '))

    # se o valor for None:
    if value is None:
        # print o erro:
        print("It isn't number.")
    # se não:
    else:
        # print o valor:
        print(f'The value is {value}.')
