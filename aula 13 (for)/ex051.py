p = int(input('Qual o primeiro termo? '))
r = int(input('\nQual a razão? '))
t = p
print()

from random import choice
import time

cores = [
    '\033[31m',
    '\033[32m',
    '\033[33m',
    '\033[34m',
    '\033[35m',
    '\033[36m',
]

for i in range(1, 11):
    cor = choice(cores)
    print(f'{cor}{t}\033[m', end='')

    for _ in range(3):
        time.sleep(0.3)
        print('.', end='')

    t += r
print('acabou!')