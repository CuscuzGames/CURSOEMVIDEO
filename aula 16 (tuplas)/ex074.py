import random

a = (1, 2, 3, 4, 5)
b = []
print(a)

for c in range(5):
    num = random.randint(1, 9)
    b.append(num)
del(a)
a = tuple(b)
print('Os valores sorteados foram:',*a)
print(f' o maior valor é {max(a)}')
print(f'O menor valor é {min(a)}')
