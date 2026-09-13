frase = input('Digíte uma frase ou uma palavra: ').upper().strip().replace(' ', '')
invertida = ''
print()
for re in range(len(frase)-1,-1,-1):
    print(frase[len(frase)-1-re],' ---> ', frase[re])
    invertida += frase[re]
print()
if frase == invertida:
    print('SIM. Isso é um palíndromo.')

else:
    print('NÃO. Isso não é um palíndromo.')