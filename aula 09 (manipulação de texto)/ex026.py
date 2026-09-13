'''Crie um programa que leia o primeiro e ultímo nome de uma pessoa.'''

nome = input('Qual o seu nome completo? ').strip()
n = nome.split()

print(f'Seu nome comleto é {nome}.')
print(f'Seu primeiro nome é {n[0]}.')
print(f'E seu ultímo nome é {n[-1]}.')
