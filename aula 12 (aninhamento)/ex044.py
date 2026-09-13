produto = float(input('Qual o preço? '))

while True:

    lista = ['DINHEIRO', 'CARTAO', '2X', '3X']
    pay = input('Qual a forma de pagamento?(Dinheiro/ Cartão/ 2x/ 3x) ').upper()
    if not pay in lista:
        print('Digite uma das opções Dinheiro, Cartao, 2x ou 3x...')
    else:
        break

if pay == 'DINHEIRO':
    print(f'Em dinheiro há um desconto de 10%. O produto sai de R${produto} e fica por R${produto-((produto/100)*10):.2f}')
elif pay == 'CARTAO':
    print(f'No cartão há um desconto de 5%. O produto sai de R${produto} e fica por R${produto-((produto/100)*5):.2f}')
elif pay == '2X':
    print(f'Você vai parcelar em duas vezes, não serão cobrado juros. Ficará duas parcelas de R${produto/2}')
else:
    print(f'Você vai parcelar em 3 vezes no cartão, será cobrado uma taxa de 20% em juros. O produto sai de R${produto} e fica por R${(20 / 100) * produto + produto:.2f}')
