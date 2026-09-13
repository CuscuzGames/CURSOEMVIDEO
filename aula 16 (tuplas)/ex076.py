print('LISTA DE PREÇOS'.center(50, '='))
print()

tab = ('CocaCola', 8.90, 'PizzaG', 40.00, 'Game', 15.99, 'GamePass', 29.99, 'Minecraft', 15.00, 'Pastel', 4.99)

for c in range(0, len(tab)):
    if c % 2 == 0:
        print(f'{tab[c]:.<20}', end= '')
    else:
        print(f'R${tab[c]:>5.2f}')
