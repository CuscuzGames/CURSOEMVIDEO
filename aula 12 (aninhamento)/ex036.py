casa = float(input('Qual o valor da casa? '))
s = float(input('Qual o seu salário? '))
anos = int(input('Em quantos anos pretende pagar? '))

p = (s / 100) * 30
t = casa / (anos * 12)

if p < t:
    print(f'''\nSeu emprestimo foi \033[1;31mnegado!\033[m
A parcela de \033[32mR${t:.2f}\033[m excede \033[33m30%\033[m do seu salário, que seria um valor de \033[32mR${p:.2f}\033[m
\nPor tanto, \033[4mnão podemos aprovar\033[m seu \033[31memprestimo.\033[m''')
else:
    print(f'''\nEmprestimo \033[1;36maprovado!\033[m
Suas parcelar vão ficar em \033[33m{anos * 12}X\033[m de \033[32mR${t:.2f}\033[m
\n\033[1;36mPARABENS PELA COMPRA!!\033[m''')
