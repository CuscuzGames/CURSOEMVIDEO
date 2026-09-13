while True:
    try:

        num = int(input(' '))
        num2 = int(input(' '))
        num3 = int(input(' '))

        maior = max(num, num2, num3)
        menor = min(num, num2, num3)

        print(f'O maior é \033[34m{maior}\033[m.')
        print(f'O menor é \033[35m{menor}\033[m.')

        break

    except ValueError:
        print('\033[31mApenas números...\033[m')
