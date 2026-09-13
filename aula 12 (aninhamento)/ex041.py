from datetime import date

ano = int(input('Em que ano você nasceu? '))
hj = date.today().year
id = hj - ano

if id <= 9:
    print(f'\nVocê tem \033[33m{id}\033[m anos. Está na categoria \033[33mMirim\033[m')
elif id <= 14:
    print(f'\nVocê tem \033[33m{id}\033[m anos. Está na categoria \033[32mInfantil\033[m')
elif id <= 19:
    print(f'\nVocê tem \033[33m{id}\033[m anos. Está na categoria \033[34mJunior\033[m')
elif id == 20:
    print(f'\nVocê tem \033[33m{id}\033[m anos. Está na categoria \033[31mSênior\033[m')
else:
    print(f'\nVocê tem \033[33m{id}\033[m anos. Está na categoria \033[35mMasters\033[m')
