import random
import time

ppt = ['PEDRA', 'PAPEL', 'TESOURA']

while True:

    j = input('Escolha: PEDRA, PAPEL ou TESOURA? ').upper().strip()
    if not j in ppt:
        print('Escolha uma das três opções: PEDRA, PAPEL ou TESOURA...')
        continue

    m = random.choice(ppt)

    print('\nPensando...')
    time.sleep(1.5)
    print(f'VOCÊ: {j}\nCOMPUTADOR: {m}')

    if j == m:
        print('EMPATOU! Jogue novamente...')
        continue
    elif j == 'TESOURA' and m == 'PAPEL':
        print('VOCÊ VENCEU!!!')
    if j == 'PAPEL' and m == 'PEDRA':
        print('VOCÊ VENCEU!!!')
    elif j == 'PEDRA' and m == 'TESOURA':
        print('VOCÊ VENCEU!!!')
    else:
        print('VOCÊ PERDEU!!!')

    while True:
        new = input('Jogar novamente?(SIM/ NÃO) ').upper().strip()
        if not new in ['SIM', 'NAO', 'NÃO']:
            print('Responda com "SIM" ou "NÃO"...')
        else:
            break

    if new == 'SIM':
        continue
    else:
        break
