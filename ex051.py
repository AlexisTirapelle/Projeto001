pTermo = int(input('Primeiro termo: '))
r = int(input('Razão: '))
for c in range(pTermo, pTermo+r*10, r):
    print(c, end=' -> ')
print('Fim.')
