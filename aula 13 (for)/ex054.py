from datetime import date

hj = date.today().year
maior = 0
menor = 0

for i in range(1, 8):
    c = int(input(f'\nEm que ano nasceu o {i}°? '))
    if hj - c >= 21:
        maior += 1
        print('É maior de idade!')

    else:
        menor += 1
        print('Não é maior de idade!')

print(f'\nHá {maior} maiores de idade.')
print(f'Há {menor} menores de idade.')
