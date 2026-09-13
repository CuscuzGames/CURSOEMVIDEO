c = 1
num = int(input(' ' ))
num2 = int(input(' '))
t = 10

while c <= t:
    print(num)
    num += num2
    c += 1

    if c > t:
        p = int(input('''\n\033[4;33mQuantos termos a mais deseja mostrar? [0 para encerrar.]\033[m
'''))

        if p == 0:
            break

        t += p

print('FIM')
