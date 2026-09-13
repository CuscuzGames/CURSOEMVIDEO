import random

cores = ['\033[31m',
         '\033[32m',
         '\033[33m',
         '\033[34m',
         '\033[35m',
         '\033[36m']
s =  0
c = 0
while True:
    cor = random.choice(cores)
    num = int(input(f'{cor}Digite um número: \033[m'))
    if num == 999:
        break
    s += num
    c += 1

print(f'\nVocê digitou \033[33m{c}\033[m números e a soma entre eles é \033[31m{s}.\033[m')
