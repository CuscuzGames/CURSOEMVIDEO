print('Vamos ver se as retas formam um triângulo e qual o tipo dele.')
import time

a = int(input('Reta A? '))
b = int(input('Reta B? '))
c = int(input('Reta C? '))

print('\n\033[33mCalculando...\033[m')
time.sleep(1.5)

if a + b > c and b + c > a and a + c > b:
    print('\nSim, essas retas podem formar um triângulo.')
    print('Mas qual o tipo de triângulo??')
    if a == b and b == c:
        print(f'''\n\033[33mReta A = {a}
Reta B = {b}
Reta C = {c}\033[m

    \033[32mTRIÂNGULO EQUILÁTERO:\033[m Todos os lados são iguais.''')
    elif a == b and a != c or b == c and b != a or c == a and c != b:
        print(f'''\n\033[33mReta A = {a}
Reta B = {b}
Reta C = {c}\033[m

    \033[34mTRIÂNGULO ISÓSCELES:\033[m Quando apenas dois lados são iguais.''')
    else:
        print(f'''\n\033[33mReta A = {a}
Reta B = {b}
Reta C = {c}\033[m

    \033[31mTRIÂNGULO ESCALENO:\033[m Todos os lados são diferentes.''')
else:
    print('\nEssas retas não podem formar um triângulo.')
