#Crie uma tupla com vários nomes aleatorios.
itens = ("game",
         "disco",
         "pendrive",
         "dvd",
         "memorycard",
         "controle",
         "tablet")

#Mostrar as vogais de cada palavra da tupla.

for palavras in itens:
    vogais = ''

    for letra in palavras:
        if letra in 'aeiou':
            vogais += letra

    print(f'Na palavra \033[34m{palavras.upper()}\033[m temos \033[33m{vogais.upper()}\033[m'if vogais else f'Na palavra \033[34m{palavras.upper()}\033[m temos \033[31mNENHUMA\033[m')
