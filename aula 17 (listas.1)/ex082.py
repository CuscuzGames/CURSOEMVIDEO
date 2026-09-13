x = []
p = []
i = []

while True:
    valores = int(input('Dígite um valor: '))
    x.append(valores)

    while True:
        op = input('Deseja dígitar outro valor? [S/N]').upper().strip()
        if not op in ['S', 'N']:
            print('Invalido! Dígite S para sim e N para não...')
        else:
            break

    if op == 'N':
        break

for c in x:
    if c % 2 == 0:
        p.append(c)

    else:
        i.append(c)

print(f'\nLISTA: {', '.join(map(str, x))}')
print(f'\nPARES: {', '.join(map(str, p))}')
print(f'\nIMPARES: {', '.join(map(str, i))}')
