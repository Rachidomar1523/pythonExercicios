import random
nc = m = n = r = 0
tupla = random.randint(1, 5), random.randint(1, 5), \
        random.randint(1, 5), random.randint(1, 5)
for r in tupla:
    nc += 1
    if nc == 1:
        m = r
        n = r
    if r > m:
        m = r
    else:
        if r < n:
            n = r
    print('Numeros sorteados: 'if nc == 1 else '', end='')
    print(r, end='')
    print(','if nc < 4 else '.', end='')
print(f'''
O maior numero sorteado foi: {m}
O menor nemero soreado foi: {n}''')
