for i in range(1, 6):
    peso = float(input(f'Quantos a {i}° pessoa pesa? '))

    if i == 1:
        maior = peso
        menor = peso

    if peso > maior:
        maior = peso

    if peso < menor:
        menor = peso

print(f'\nO mais gordo da lista: {maior}')
print(f'O mais magro da lista: {menor}')
