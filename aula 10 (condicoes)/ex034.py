while True:
    try:


        salario = float(input('Qual o salário? '))
        a = (salario / 100) * 10
        b = (salario / 100) * 15

        if salario >= 1250:
            print(f'''O funcionario recebe \033[32mR${salario}\033[m e terá um aumento de \033[33m10%\033[m, o equivalente a \033[32mR${a:.2f}\033[m
Com esse aumento seu salário passou a ser \033[32mR${salario + a:.2f}\033[m''')

        else:
            print(f'''O funcionario recebe \033[32mR${salario}\033[m e terá um aumento de \033[33m15%\033[m, o equivalente a \033[32mR${b:.2f}\033[m
Com esse aumento o salário passou a ser \033[32mR${salario + b:.2f}\033[m''')

        break

    except ValueError:
        print('\033[31mApenas números.\033[m')
