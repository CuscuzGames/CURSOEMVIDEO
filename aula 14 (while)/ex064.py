num = 0
s = 0
q = 0
c = 1

while num != 999:
    try:
        num = int(input(f'Digíte o {c}° número: '))
    except:
        print('Apenas números.')
        continue

    c += 1
    s += num
    q += 1

print(f'\nA soma dos números é \033[33m{s - 999}\033[m')
print(f'\nVocê digítou \033[33m{q - 1}\033[m vezes.')
