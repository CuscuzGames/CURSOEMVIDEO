m = f = 0
p = ''

while p != 'ENCERRAR':
    p = input('''Qual o sexo da pessoa? [M/F ou ENCERRAR para fechar o programa.]
    ''').upper()

    if not p in ['M', 'F', 'ENCERRAR']:
        print('Essa resposta é invalida!')

    elif p == 'M':
            m += 1

    elif p == 'F':
         f += 1

print(f'Há {m} homens e {f} mulheres.')
