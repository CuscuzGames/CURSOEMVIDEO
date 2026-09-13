m = 0
f = 0
t = 0

for i in range(1, 6):
    nome = input(f'\nQual o nome dá {i}° pessoa? ')
    idade = int(input('Qual a idade? '))
    sexo = input('Qual o sexo? (M/F)').upper().strip()
    t += idade

    if sexo == 'M' and idade < 20:
        m += 1

    if sexo == 'F' and idade < 20:
        f += 1

    if i == 1:
        maior = idade
        menor = idade
        velho = nome
        novo = nome

    if idade > maior:
        maior = idade
        velho = nome

    if idade < menor:
        menor = idade
        novo = nome

t /= i
print(f'\nMais velho:{velho}.  Idade:{maior}')
print(f'Mais novo:{novo}.  Idade:{menor}')
print(f'Quantos Homens tem menos de 20: {m}')
print(f'Quantas mulheres tem menos de 20: {f}')
print(f'A média entre as idades: {t}')
