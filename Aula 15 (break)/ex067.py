while True:
    num = int(input('\nDigite um número: '))
    if num < 0:
        break

    print(f'\nA tabuáda do número {num} é:')
    print()
    for tabuada in range(1, 11):
        print(f'{num} x {tabuada} = {num*tabuada}')

    print(f'\nA tabuada de divisão do número {num} é:')
    print()
    for dividindo in range(1, 11):
        print(f'{num} / {dividindo} = {num/dividindo:.2f}')

print('Programa encerrado!')
