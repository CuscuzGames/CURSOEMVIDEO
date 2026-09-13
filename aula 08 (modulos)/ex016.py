import math

while True:
    n = float(input("Digite um numero real? "))
    i = math.trunc(n)

    if n < 0:
        print("COMANDO ENCERRADO!")
        break

    else:
        print(f"O numero {n} tem como sua parte inteira {i}")
