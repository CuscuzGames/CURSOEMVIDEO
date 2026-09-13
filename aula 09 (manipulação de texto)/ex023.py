num = int(input('Digíte um número: '))
n = str(num)

if num > 9999 or num < 0:
    print('\033[37mNúmero invalido!\033[m')

else:
    m = (num // 1000) % 10
    c = (num // 100) % 10
    d = (num // 10) % 10
    u = num % 10
    print(f'''\033[31mU.Mlhar: {m}\033[m
    \033[32mCentenas: {c}\033[m
    \033[33mDezenas: {d}\033[m
    \033[35mUnidades: {u}\033[m''')
