'''Crie um programa que leia o nome de uma cidade e diga se
ela começa ou não com o nome "SANTO".'''

city = input('Qual a cidade? ').upper().strip()

print(f'{city}')
s = city.split()
print(f'O primeiro nome é {s[0]}')
print('SANTO' in s[0])

if not s[0] == 'SANTO':
    print('Não se inicia com Santo.')
else:
    print('Sim, começa com Santo.')
