while True:
    while True:
        pergunta = input('Impar ou Par? ').upper().strip()
        if pergunta in ['IMPAR', 'PAR']:
            break
        else:
            print('Responda com Impar ou Par.')


    if pergunta == 'IMPAR':
        for num in range(1, 51, 2):
            print(num)

    else:
        for num in range(2, 51, 2):
            print(num)
    break
