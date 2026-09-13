num = ('Zero', 'Um', 'Dois', 'Três', 'Quatro',
       'Cinco', 'Seis', 'Sete', 'Oito',
       'Nove', 'Dez', 'Onze', 'Doze',
       'Treze', 'Quatorze', 'Quinze', 'Dezesseis',
       'Dezessete', 'Dezoito', 'Dezenove', 'Vinte')

while True:
    try:
        p = int(input('Digíte um número de 1 a 20: '))
        if 0 > p or p > 20:
            print('Número invalido! Digíte um número entre 1 e 20...')
        else:
            print(f'\nO numero que vc digitou foi {num[p]}')
            break

    except ValueError:
        print('\nDigite apenas números.')
