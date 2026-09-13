l = []
p = []

for c in range(4):
    while True:
        num = int(input('\nDigite um número de 1 a 9: '))
        if 0 < num < 10:
            break
        else:
            print('\nValor invalido! ')
    l.append(num)
    if num % 2 == 0:
        p.append(num)

t = tuple(l)
lol = tuple(p)
print()
print('=-'*30)
print(f'\nOs valores digitados foram: {', '.join(map(str, t))}')
print(f'O numero nove foi digitado {t.count(9)} vezes.')
if not 3 in t:
    print('O valor 3 não foi digitado em nenhuma posição.')
else:
    print(f'O número três apareceu na {t.index(3)+1}° posição.')
print(f'Os números pares são: {', '.join(map(str, lol))}')
