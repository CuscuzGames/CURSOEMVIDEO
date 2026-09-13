'''Faça um programa que leia uma frase e diga quantas letras "A" tem na frase, quando aparece primeiro e em ultimo.'''

texto = input(' ').upper().strip()

print(f'\nQuantidade de letras "A´s": {texto.count('A')}')
print(f'\nQuando aparece a primeira vez: {texto.find('A')}')
print(f'\nQuando aparece pela ultima vez: {texto.rfind('A')+1}')

