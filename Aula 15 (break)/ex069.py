h = 0
m = 0
p = 0
t = 0
f = 0

while True:
    try:
        idade = int(input('Qual a idade da pessoa? '))
        if idade < 0:
            print('Invalido!')
            continue
    except ValueError:
        print('Digite apenas números...')
        continue
    while True:

        sexo = input('Qual o sexo? [M/F] ').upper().strip()
        if sexo in ['M','F']:
            break
        else:
            print('Digite M para masculino ou F para feminino.')
    while True:

        o = input('Você deseja continuar? [S/N] ').upper().strip()
        if o in ['S','N']:
            break
        else:
            print('Digite S para sim ou N para não.')

    t += 1

    if idade > 18:
        p += 1

    if sexo == 'M':
        h +=1

    if sexo == 'F' and idade < 20:
        m += 1

    if sexo == 'F':
        f += 1

    if o == 'S':
        continue

    if o == 'N':
        break

print(f'''O total de pessoas foi {t}.
{p} eram, maiores de 18.
{h} eram homens.
{f} eram mulheres.
{m} eram mulheres menores de 20 anos.''')
