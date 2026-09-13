while True:
    try:

        num = int(input('Digíte um número qualquer: '))
        n = num % 2

        if n == 0:
            print('\033[33mEsse número é par!\033[m')
        else:
            print('\033[34mEsse numero é impar!\033[m')

        break

    except ValueError:
        print('\033[31mApenas números...\033[m')
