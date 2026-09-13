import random

while True:
    lista = ["Jão",
             "Esther",
             "Zaraki",
             "Goku",
             "Perseu",
             "Galatico",
             "Goku",
             "Seya",
             "Inuyasha",
             "Erza",
             "Gojo"]
    sorteado = random.choice(lista)
    print(f"{sorteado} foi o vencedor!!")

    if "Gojo" == sorteado:
        print(f"Satoro {sorteado}, o mais honrado, encerrou esse programa!")
        break
