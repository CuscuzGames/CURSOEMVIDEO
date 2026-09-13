import math

a = int(input("Qual o ângulo? (45°, 60°, 90°) "))
rad = math.radians(a)
sen = math.sin(rad)
cos = math.cos(rad)
tan = math.tan(rad)

if a in [45, 60]:
    print(f"""SENO: {sen:.2f}

COSSENO: {cos:.2f}

TANGENTE: {tan:.2f}""")

elif a == 90:
    print(f"""SENO: {sen:.2f}

COSSENO: {cos:.2f}

TANGENTE: Inexistente!""")

else:
    print("Numero invalido!")
