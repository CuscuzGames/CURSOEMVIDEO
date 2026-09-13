q = input('Digíte a expressão: ')
p = []

for s in q:
    if s == '(':
        p.append('(')
    elif s == ')':
        if len(p) > 0:
            p.pop()
        else:
            p.append(')')
            break

if len(p) == 0:
    print('Sua equação está correta!')
else:
    print('Sua equação está incorreta!')
