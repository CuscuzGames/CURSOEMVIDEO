num = int(input(''))
e = num

for c in range(num-1, 1, -1):
    e *= c
    print(e)

print(f'\n{e}')

print()
print('-='*20)
print()
f = 1
while num > 1:
    f *= num
    print(f)
    num -= 1

print(f'\n{f}')
