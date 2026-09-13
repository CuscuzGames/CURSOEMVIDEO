print('<>'*40)
print('BANCO DO CLARENCIO'.center(50))
print('<>'*40)

while True:
    try:

        saque = int(input('\nQuantos dinheiros do Clarencio você deseja sacar? '))
        if saque < 0:
            print('Esse valor é inválido!')
            continue

    except ValueError:
        print('Apénas números...')
        continue

    c = saque // 50
    v = (saque - (c*50)) // 20
    d = (saque - ((c*50)+(v*20))) // 10
    u = saque % 10

    print(f'''\nO valor sacado foi {saque}
\nTotal de {c} cédulas de R$50
Total de {v} cédulas de R$20
Total de {d} cédulas de R$10
Total de {u} cédulas de R$1''')
    print()
    print('<>'*40)

    op = input('\nDeseja sacar mais dinheiro do Clarencio? [S/N] ').upper().strip()

    if not op in ['S', 'N']:
        print('Responda com S para sim ou N para não.')

    elif op == 'N':
        break

    else:
        print()

print('\nPrograma encerrado!')
