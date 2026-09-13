# Dolar

while True:

    c = float(input("Quatos em reais a pessoa tem? (Numeros Negativos encerra o programa) "))
    d = 3.27
    t = c / d

    if c < 0:
     print("PROGRAMA ENCERRADO!")
     break

    else:
     print(f"""Se a pessoa tem R${c} reais e o dolar vale U${d}.
     Então o maximo que se pode comprar é {t:.2f}""")
