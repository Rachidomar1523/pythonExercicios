n1 =[]
n2 = []
n3 = []
while True:
    n = int(input('Digite um numero: '))
    n1.append(n)
    nq = str(input('Queres continuar: ')).upper()
    while nq not in 'NS':
        nq = str(input('Opçao invalida [S/N]:')).upper()
    if nq == 'N':
        break
    for m in n1:
        if m % 2 == 0:
            m1 = m
            n1.append(m1)
        else:
            m2 = m
            n1.append(m2)
print(f'''voce digitou {n1}
listas dos pares {n2}
listas dos inpares {n3}''')

