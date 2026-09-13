while True:
     try:

        num = int(input('Escolha um número: '))
        if num < 0:
            break

        print(f'\nMultiplicando o número {num}')
        print()
        for i in range(1, 11):
            print(f'\033[34m{num}\033[m x \033[33m{i}\033[m = \033[31m{num * i}\033[m')

        print(f'\n Dividindo o número {num}')
        print()
        for d in range(1, 11):
            print(f'\033[35m{num}\033[m / \033[36m{d}\033[m = \033[37m{num / d:.2f}\033[m')
        print()
     except ValueError:
         print('Digíte apenas números.')
