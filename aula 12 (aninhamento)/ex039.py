from datetime import date

while True:
    try:

        ano = int(input('\033[33mEm que ano você nasceu? \033[m'))
        hj = date.today().year
        id = hj - ano

        if id < 18:
            print(f'Você tem \033[37m{id}\033[m anos.Ainda faltam {18 - id} ano/s para se alistar.')
        elif id == 18:
            print(f'Você tem \033[34m{id}\033[m anos. Está na hora de fazer o alistamento Militar.')
        else:
            print(f'Você tem \033[31m{id}\033[m anos.Passou {id - 18} ano/s do prazo. Terá que pagar uma multa!')

        break

    except ValueError:
        print('Apenas numeros...')
