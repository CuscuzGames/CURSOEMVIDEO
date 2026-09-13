#Crie um programa onde o usuario possa digitar cinco valores.

kof = []

for v in range(5):
    while True:
        try:
            valores = int(input(f'Digite o {v}° valor: '))
            if valores < 0:
                print('Valor invalido!')
            else:
                break

        except ValueError:
            print('Digíte apenas números...')

#Adiciona o primeiro valor a lista.
    if v == 0:
        kof.append(valores)
        print('Foi adicionado a lista.')

#Se for maior ou igual ao ultimo vai para o final da lista.
    elif valores >= kof[-1]:
        kof.append(valores)
        print('Foi adicionado ao final da lista.')

#Se for menor ou igual ao primeiro vai para o inicio da lista.
    elif valores <= kof[0]:
        kof.insert(0, valores)
        print('Foi adicionado no inicio da lista.')

#Se estiver no meio, pecorre até encontrar.
    else:
        for i in range(len(kof)):
            if valores <= kof[i]:
                kof.insert(i, valores)
                print(f'Foi adicionado na posição {i}.')
                break

print(kof)
