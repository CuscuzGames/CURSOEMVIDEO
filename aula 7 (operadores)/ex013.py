# Salario

while True:
    s = float(input("Qual o seu salario? R$ "))
    a = int(input("Em quantos por cento vai aumentar? %"))
    p = s * (a/100)
    t = s + p

    if s < 0:
        print("ENCERRADO!!!")
        break

    else:
        print(f"O salario recebeu um aumento de {a}%")
        print(f"O salario saiu de R${s} e foi para R${t}")
