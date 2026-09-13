viagem = int(input('Quantos Km tem a viagem? '))
a = viagem * 0.50
b = viagem * 0.45

if viagem <= 200:
    print(f'Sua passagem custará \033[32mR${a}\033[m\n Faça uma boa viagem!')
else:
    print(f'Sua passagem custará \033[32mR${b}\033[m\n Faça uma boa viagem')
