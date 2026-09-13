a = int(input('Lado A? '))
b = int(input('Lado B? '))
c = int(input('Lado C? '))

if a + b > c and b + c > a and c + a > b:
    print('\033[1;36mSIM!\033[m Essas retas formam um triângulo.')
else:
    print('\033[1;31mNÃO!\033[m Essas retas não formam um triângulo.')
