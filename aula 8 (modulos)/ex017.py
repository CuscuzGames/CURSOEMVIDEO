import math

print("Descubra o valor do Cateto A")
print("A = H² -  B²")

h = float(input("\nDigite o valor da hipotenusa: "))
print(f"\nO valor da Hipotenusa é {math.trunc(h)}")
c = float(input("\nDigite o valor do Cateto B: "))
print(f"\nO valor do Cateto B é {math.trunc(c)}")
eh = math.trunc(h) ** 2
ec = math.trunc(c) ** 2
r = eh - ec

print(f"\nO resultado do Cateto A é {math.sqrt(r):.2f}")

print(""" \nAo fazer o calculo da hipotenusa ao quadrado e tambem o Cateto B ao quadrado, basta
pegar o resultado e subtrair a hipotenusa pelo Cateto B. Depois disso, é só calcular a raiz quadrada do numero.

EX.: Hipotenusa = 8²
     Cateto B = 4²
A fómula ficaria: Ca = 8² - 4²
                  Ca = 64 - 16
                  Ca = √48
                  Ca = 6,92
    
FIM.""")

co = float(input("Qual o Cateto oposto? "))
ca = float(input("Qualo Cateto adjacente? "))
hi = math.hypot(co, ca)

print(f"O valor da Hipotenusa é {hi:.2f}")
