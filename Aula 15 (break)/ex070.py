print('-'*40)
print('LOJÃO DE PYTHON'.center(40))
print('-'*40)
print()
total = 0
c = 0
caro = 0

while True:
    produto = input('Qual o produto? ')
    try:
        while True:
            preco = float(input('Qual o preço? R$'))
            if preco < 0:
                print('Valor invalido!')
            else:
                break

    except ValueError:
        print('Apenas números!')

    while True:
        o = input('Você deseja continuar com as compras? [S/N] ').upper().strip()
        if o in ['S','N']:
            break
        else:
            print('Digite apenas S ou N')

    total += preco

    if c == 0:
        barato = preco
        nom = produto

    if preco < barato:
        barato = preco
        nom = produto

    if preco >= 1000:
        caro += 1

    c += 1

    if o == 'N':
        break
print()
print('-'*45)

print(f'O Total de suas compras foi {total:.2f}')
print(f'O produto mais barato é {nom} e custou {barato}')
print(f'{caro} produtos custaram acima de R$1000,00')
