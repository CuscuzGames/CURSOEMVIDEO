while True:

    n = int(input("Digite um numero: "))
    if n < 0 :
        print("Programa encerrado.")
        break

    print(f"\nTabuada do numero {n}:")
    print()
    for tabuada in range(1, 11):
        print(f"{n} x {tabuada} = {n * tabuada}")
    print()
