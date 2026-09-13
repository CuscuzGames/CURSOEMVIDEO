import random

lista = ["Ryu", "Ken", "Chun-li", "Cammy"]

s = random.sample(lista, 4)

for i, nome in enumerate(s, start=1):
    print(f"{i}° Sorteio: {nome}")
