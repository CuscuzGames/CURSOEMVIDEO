peso = float(input('Quantos você pesa? '))
altura = float(input('Qual a sua altura? '))
imc = peso / (altura * altura)

print(f'PESO: {peso}')
print(f'ALTURA: {altura}')
print(f'IMC: {imc:.2f}')
if imc <= 18.5:
    print('Você está abaixo do peso. Precisa ganhar ums quilinhos kkk')
elif imc <= 25:
    print('Você está deliciosamente mo peso ideal. Continue goxtoso kk')
elif imc <= 30:
    print('Hm, você está com sobrepeso, precisa fazer uns exercícios.')
elif imc <= 40:
    print('Você tem uma placa no MC Donalts escrito: "Proibido Alimentar!"...')
else:
    print('Você tem orbita propría, a Nasa já está planejando a exploração do novo planeta que é VOCÊ!')
