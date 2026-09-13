a = int(input('\033[33mQual o valor A? \033[m'))
b = int(input('\033[35mQual o valor B?\033[m '))
maior = max(a, b)
menor = min(a, b)

if a == b:
    print(f'Os valores \033[33m{a}\033[m e \033[35m{b}\033[m são iguais.')
else:
    print(f'O valor maior é \033[1;36m{maior}\033[m.\nE o menor é \033[1;31m{menor}\033[m.')
