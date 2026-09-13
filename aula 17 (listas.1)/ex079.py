#Crie um programa em que o usuário possa digitar varios valore e salvá-los em uma lista.
valores = []

while True:
    try:
        num = int(input('\nDigite um número: '))
        if not num in valores:
            valores.append(num)
        else:
            print('Esse número já foi digitado. Escolha outro...')
            continue
    except ValueError:
        print('Invalido! Digíte apenas números...')
        continue

    while True:

        escolha = input('\nDeseja continuar adicionando? [S/ N]').upper().strip()
        if not escolha in ['S','N']:
            print('Invalido! Digíte S para sim e N para não.')
        else:
            break

    if escolha == 'S':
        continue
    else:
        break

print()
print(sorted(valores))