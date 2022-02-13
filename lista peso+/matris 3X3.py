c = f1 = f2 = f3 = mais = c3 = p = 0
l = [[], [], [], [], [], [], [], [], []]
li = []
for d in range(0, 9):
    c += 1
    n = int(input(f'Digite um valor para a posiçao {c}: '))
    l[d].append(n)
    if c <= 3:
        f1 += n
    else:
        if 3 < c <= 6:
            f2 += n
            mais = n
            if n > mais:
                mais = n
        if 6 < c <= 9:
            f3 += n
    if n % 2 == 0:
        p += n
    if d == 2:
        c3 += n
    else:
        if d == 5:
            c3 += n
        if d == 8:
            c3 += n
    print(d)
o = 0
print(f'{"MATRIS 3X3":*^50}')
for r in range(0, 9):
    o += 1
    print(f'       {l[r]}', end='')
    print('', end='')
    if o == 3:
        print('\n')
    else:
        if o == 6:
            print('\n')
print(f'\n{"MATRIS 3X3":*^50}')
print(f'''{"soma dos valores da 1ª Fila":<1}{":":>13} {f1:>5}
{"soma dos valores da 2ª Fila":<1}{":":>13}{f2:>6}
{"soma dos valores da 3ª Fila":<1}{":":>13}{f3:>6}
{"soma dos valores pares":<1}{":":>18}{p:>6}
{"O maior valor da 2ª fila":>1}{":":>16}{mais:>6}
{"soma dos valores da terceira coluna"}{":":>5}{c3:>6}''')
print(f'{"MATRIS 3X3":*^50}')