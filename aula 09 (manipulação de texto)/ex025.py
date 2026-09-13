nome = input('Digíte seu nome completo: ').upper()

if 'SILVA' in nome :
    print('\033[33mSIM\033[m, você é um dos Silvas.')
else:
    print('\033[31mNÃO\033[m, você não é um dos Silvas.')
