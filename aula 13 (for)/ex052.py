while True:

    num = int(input("Digíte um número? "))

    d = 0

    for op in range(1, num+1):

        if num % op == 0:
            d += 1

    if num == 0:
        print('Programa encerrado!')
        break

    if d == 2:
        print('Número primo')

    else:
        print('Não é primo')
