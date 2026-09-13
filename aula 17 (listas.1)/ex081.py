joja = []
c = 0

while True:

    num = int(input('\nDigite um valor: '))
    joja.append(num)
    c += 1

    while True:
        op = input('Deseja digitar outro valor? [S/ N] ').upper().strip()
        if not op in ['S','N']:
            print('Invalido! Dígite S para sim e N para não...')

        else:
            break

    if op == 'N':
        break

print(joja)
joja.sort(reverse=True)
print(joja)
print(f'Você dígitou {c} números.')
if 5 in joja:
    print(f'Sim, o número 5 foi dígitado na posição {joja.index(5)}')

else:
    print('Não encontrei o número 5 na lista...')
