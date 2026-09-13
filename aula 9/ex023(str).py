'''Faça um programa que leia um numero de 0 a 9999 e
mostre na tela cada um dos digitos separados.

Ex.: Num: 1834
Unidades: 4
Dezenas: 3
Centenas: 8
U. Milhar: 1'''

num = int(input('\nDigíte  um numero dentre 0 e 9999: '))

if num > 9999:
    print('Invalido! Esse numero excede o limite!')
elif num < 0:
    print('Invalido! Esse numero é insuficiente!')
else:
    u = num % 10
    d = (num // 10) % 10
    c = (num // 100) % 10
    m = (num // 1000) % 10

    print(f'''U. Milhar = {m}
Centenas = {c}
Dezenas = {d}
Unidade = {u}''')

'''Agr em String'''

num2 = input('\nDigite um numero de 0 a 9999: ')

if not num2.isdigit() or int(num2) > 9999:
    print('Número inválido!')
else:
    num2 = num2.zfill(4)
    print(f'''U. Milhar = {num2[0]}
Centenas = {num2[1]}
Dezenas = {num2[2]}
Unidades = {num2[3]}''')
