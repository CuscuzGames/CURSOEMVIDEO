times = ('PALMEIRAS', 'FLAMENGO', 'FLUMINENSE', 'BRAGANTINO', 'ATLETICO-PR',
         'BAHIA', 'CORITIBA', 'SÃO PAULO', 'BOTA FOGO', 'VITORIA',
         'ATLETICO-MG', 'CORINTHIANS', 'CRUZEIRO', 'INTERNACIONAL', 'SANTOS',
         'GREMIO', 'VASCO', 'MIRASSOL', 'REMO', 'CHAPECOENSE'
         )


ltimes = list(times)
ltimes.sort()
alfatimes = tuple(ltimes)

print('!!!OS CINCOS PRIMEIROS!!!'.center(50, '='))
print()
for p, c in enumerate(times[0:5], start = 1):
    print(f'{p}° {c}')
print()
print('='*40)

print()
print('!!!OS QUATRO ULTIMOS!!!'.center(50, '='))
print()
for p, c in enumerate(times[16:21], start= 17):
    print(f'{p}° {c}')
print()
print('='*40)

print()
print('Lista em ordem alfabetica'.center(50, '~'))
print()
for p, c in enumerate(alfatimes):
    print(c)
print()
print('~'*40)

print()
tab = input('Qual time você quer ver a posição? ').upper()
if tab in times:
    print(f'\nO time {tab} está em {times.index(tab)+1}° lugar.')

else:
    print('\nEsse time não está na tabela.')
