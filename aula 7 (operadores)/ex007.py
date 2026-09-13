# Media
aluno = input("Qual o nome do aluno? ")
n1 = float(input("Qual a primeira nota? "))
n2 = float(input("Qual a segunda nota? "))
m = (n1 + n2) / 2

print(f"A media de {aluno} foi de {m}")

if m >= 7:
    print(f"PARABÈNS! O ALUNO {aluno} FOI APROVADO!!")
elif m >= 5:
    print(f"O aluno {aluno} ficou de recuperação.")
else:
    print(f"O aluno {aluno} foi reprovado! Estude mais.")
