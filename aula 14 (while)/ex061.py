import random
import time

num = int(input(' '))
num2 = int(input(' '))
r = num
c = 0

cores = ['\033[31m',
         '\033[32m',
         '\033[33m',
         '\033[34m',
         '\033[35m',
         '\033[36m',
         ]

while c < 10:
    cor = random.choice(cores)
    print(f'{cor}{r}\033[m', end='', flush=True)
    for _ in range(3):
        time.sleep(0.3)
        print('.', end='', flush=True)
    r += num2
    c += 1
