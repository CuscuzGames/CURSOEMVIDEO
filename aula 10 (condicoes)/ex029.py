vel = int(input('Qual a velocidade do veículo? '))

if 41 <= vel <= 80:
    print('\033[32mTudo cero, continue dentro da lei.\033[m')
elif vel <= 40:
    print('\033[35mMinha Vó corre mais que essa banheira ai HAHAHA!!\033[m')
else:
    multa = (vel - 80) * 7
    print(f'''\033[33mVocê ultrapassou o limíte de velocidade!
Sua multa será de\033[m \033[31mR${multa} merreis!\033[m''')