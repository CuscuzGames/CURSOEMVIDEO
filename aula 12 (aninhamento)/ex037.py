# BINARIO, OCTAL & HEXADECIMAL

while True:
    try:
        num = int(input('Digite um número: '))
        break
    except ValueError:
        print('Apenas números!')

while True:
    try:
        op = int(input('''Escolha: 
1 para converter em binário
2 para converter em Octal
3 para converter em eHexadecimal
 '''))
        if not op in [1, 2 , 3]:
            print('Escolha uma das opções:')
            continue
        else:
            break

    except ValueError:
        print('DIGITE APENAS NÚMEROS!')

if op == 1:
    print(f'O número {num} em Binário seria: {bin(num)[2:]}')
elif op == 2:
    print(f'O número {num} em Octal seria: {oct(num)[2:]}')
else:
    print(f'O número {num} em Hexadecimal seria: {hex(num)[2:]}')
