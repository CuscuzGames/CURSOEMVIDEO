r = ''
c = 0
s = 0

while r != 'N':
    try:
        v = int(input('Didite um valor: '))
    except:
        print('Apenas números!')
        continue

    if c == 0:
        maior = menor = v
    else:
        if v > maior:
            maior = v
        if v < menor:
            menor = v

    s += v
    c += 1
    r = input('Deseja continuar? [S para Sim/ N para não]').upper().strip()
    if r == 'S':
        continue

    elif not r in ['S', 'N']:
        print('Digíte apenas S ou N.')
        while r != ['S','N']:

            r = input('Dseja continuar? [S para sim/ N para Não]').upper().strip()
            if not r in ['S', 'N']:
                print('Invalido! Apenas S ou N.')
            if r == 'S':
                break
            if r == 'N':
                break
            else:
                continue

    else:
        print('Programa encerrado.')

print(f'\nA soma dos valores digítados é de {s}')
print(f'A quantidade de números que você digítou foi {c}')
print(f'A média entre os números é de {s/c:.2f}')
print(f'O maior número é {maior}')
print(f'O menor número é {menor}')
