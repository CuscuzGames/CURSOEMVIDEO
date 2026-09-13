nome = input('').strip()
nome1 = nome.split()

'''Nome com todas as letras maiusculas.'''

print(nome.upper())

'''Nome com todas as letras minusculas.'''

print(nome.lower())

'''Quantas letras ao todo sem considerar os espaços?'''

print(len(nome.replace(' ', '')))

'''Quantas letras tem o primeiro nome?'''

print(len(nome1[0]) if nome1 else 0)