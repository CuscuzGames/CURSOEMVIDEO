num = int(input('''Digíte um número: 
 '''))

a = 0
b = 1
c = 0

while c < num:
    print(f'\033[34m{a}\033[m', end=' \033[33m->\033[m ')
    a, b = b, a + b
    c += 1
print('FIM.')