soma = 0

for n in range(1, 7):
    num = int(input(f'Diíte o {n}° número: '))
    if num % 2 == 0:
        soma += num

print()
print(soma)
