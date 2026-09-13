p = 0
num = int(input('Digíte um número: '))
num2 = int(input('Digíte um segundo número: '))

while p != 7:

    p = int(input('''
    [1] +            [2] -
    [3] *            [4] /
    [5] Maior        [6] Novos Valores
    [7] Encerrar
    
    Ecolha uma opção para continuar:  '''))

    if p == 1:
        print(f'\nA soma de {num} + {num2} é {num+num2}')

    elif p == 2:
        print(f'\nA subtração de {num} - {num2} é {num-num2}')

    elif p == 3:
        print(f'\nA multiplicação de {num} * {num2} é {num*num2}')

    elif p == 4:
        print(f'\nA divisão de {num} / {num2} é {num/num2:.2f}')

    elif p == 5:
        print(f'\nO maior número entre {num} e {num2} é {max(num, num2)}')

    elif p == 6:
        num = int(input('Digíte um novo valor: '))
        num2 = int(input('Digíte um segundo novo valor: '))

    else:
        print('Programa encerrado!')
