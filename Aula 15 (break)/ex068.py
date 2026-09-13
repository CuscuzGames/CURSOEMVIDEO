import random

c = 0

while True:
    m = random.randint(1, 10)
    try:
        j = int(input('Digite um valor: '))
        if j < 0:
            print('\n\033[33mValor invalido! Tente novamente...\033[m')
            continue

    except ValueError:
        print('\n\033[31mDigite apenas números.\033[m')
        continue

    while True:

        a = input('\nIMPAR OU PAR? \033[36m[P/ I]\033[m').upper().strip()
        if a in ['P', 'I']:
            break
        print('\n\033[33mDigite apenas "I" para ímpar ou "P" para par.\033[m')

    s = m + j

    print(f'\n\033[34mJogador\033[m escolheu \033[34m{j}\033[m e \033[35mmaquina\033[m escolheu \033[35m{m}\033[m\nO resultado é \033[33m{s}\033[m.')

    if s % 2 == 0 and a == 'P':
        print('\n\033[32mDeu par. Você venceu.\033[m')

    if s % 2 == 1 and a == 'I':
        print('\n\033[32mDeu impar. Você venceu!\033[m')

    if s % 2 == 0 and a == 'I':
        print('\n\033[37mDeu par. Você perdeu...\033[m')
        break

    if s % 2 == 1 and a == 'P':
        print('\n\033[37mDeu impar. Você perdeu...\033[m')
        break

    c += 1

print(f'\n\033[33mGAME OVER!\033[m\n\033[33mRecorde: {c}\033[m')
