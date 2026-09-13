# VAMOS FAZER CONTAS!!!

print("Aprendendo contas basicas em Python.")

# Adição= (+) Subtração= (-) Multiplicação= (*) Divisão= (/)

n1 = int(input("Qual o primeiro número? "))
n2 = int(input("Qual o segundo número? "))
a = n1 + n2
s = n1 - n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2
r = n1 % n2

print(f"Resultado da soma de {n1} e {n2} é: {a}")
print(f"Resultado da subtração de {n1} e {n2} é: {s}")
print(f"Resultado da multiplicação de {n1} e {n2} é: {m}")
print(f"Resultado da divisão de {n1} e {n2} é: {d:.2f}")
print(f"Resultado da divisão inteira de {n1} e {n2} é: {di}")
print(f"Resultado da exponenciação de {n1} e {n2} é: {e}")
print(f"Resultado do resto da divisão de {n1} e {n2} é: {r}")
