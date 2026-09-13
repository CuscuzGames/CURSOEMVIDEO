s = 0
c = 0

for n in range(3, 501, 3):
    if n % 2 == 1:
        print(n)
        s += n
        c += 1

print(f'A soma total é: \033[31m{s}\033[m')
print(c)