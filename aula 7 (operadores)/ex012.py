# Desconto
while True:
    p = float(input("Qual o valor do produto? R$ "))
    d = p * (5/100)
    t = p - d

    if p < 0:
        print("ENCERRADO!!")
        break

    else:
        print(f"Com o desconto de 5% o produto sái a R${t:.2f} ")
