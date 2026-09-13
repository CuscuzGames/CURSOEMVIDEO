from datetime import date

while True:
    try:

        ano = int(input('Digite um ano qualquer: '))
        if ano == 0:
            ano = date.today().year
        if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
            print(f'{ano} é \033[33mBISSEXTO!\033[m')
        else:
            print(f'{ano} não é \033[37mBISSEXTO!\033[m')

        break

    except ValueError:
        print('\033[31mDigíte números...\033[m')
