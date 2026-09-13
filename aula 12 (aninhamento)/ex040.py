while True:
    try:

        nota1 = float(input('Qual a primeita nota? '))
        if 0 <= nota1 <= 10:
            break
        else:
            print('Inválido! Digite uma nota de 0 a 10...')
    except ValueError:
        print('Apenas números...')

while True:
    try:

        nota2 = float(input('Qual a segunda nota? '))
        if 0 <= nota2 <= 10:
            break
        else:
            print('Inválido! Digite uma nota de 0 a 10...')
    except ValueError:
        print('Apenas números...')

m = (nota1 + nota2) / 2

print(f'\nSua média foi de \033[1;33m{m}\033[m')
print('')

if m >= 7:
    print('\033[32m( ＾∇＾)\033[m' * 10)
    print('\n\033[1;36mPARABÉNS!\033[m Você foi Aprovado!')
    print('')
    print('\033[32m( ＾∇＾)\033[m' * 10)

elif m >= 5:
    print('\033[33m(•ิ_•ิ\033[m)' * 10)
    print('\n\033[4;33mVocê ficou de Recuperação...\033[m Se esforce mais na proxima!')
    print('')
    print('\033[33m(•ิ_•ิ)\033[m' * 10)

else:
    print('\033[37m(╥﹏╥)\033[m' * 10)
    print('\n\033[1;31mREPROVADO!\033[m Conseguiu decepcionar todos que acreditaram em você... Espero que esteja orgulhoso...')
    print('')
    print('\033[37m(╥﹏╥)\033[m' * 10)
