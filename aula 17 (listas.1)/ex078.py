#Faça um for que leia cinco valores e guarde-os em uma lista.

num = []

while True:

    for c in range(1, 6):
        while True:
            try:
                valores = int(input(f'Digite o {c}° valor: '))

                num.append(valores)
                break

            except ValueError:
                print('Digite apenas números...')

    print('\nLISTA:', end=' ')
    print(', '.join(map(str, num)))

    #Mostre o maior e o menor valor dessa lista.

    maior = max(num)
    menor = min(num)

    print(f'\nO maior número da lista é: \033[36m{maior}\033[m⬆️')
    print(f'O menor número da lista é: \033[35m{menor}\033[m⬇️')

    #Mostre a posição em que eles se encontram na lista.

    print('\nOs maiores valores se encontram nas posições: ',end='')
    for posicao, valor in enumerate(num, start=1):
        if valor == maior:
            print(f'{posicao}', end=', ')

    print('\nOs menores valores se encontram nas posições: ',end='')
    for posicao, valor in enumerate(num, start=  1):
        if valor == menor:
            print(f'{posicao}', end=', ')

    #Comando para reiniciar.

    while True:
        print()
        inicio = input('''\nDeseja reiniciar o exercício? [S/ N]
  ''').upper().strip()
        if not inicio in ['S', 'N']:
            print('Invalido! Digite S para sim e N para não.')

        else:
            break

    if inicio == 'S':
        print('\nReiniciando')
        del num
        num = []
        print()

    else:
        print('\nPrograma encerrado.')
        break
