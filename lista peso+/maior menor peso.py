c = ca = 0
l = []
while True:
    c += 1
    n = input(f'Nome da {c}ª pessoa: ').upper().split()[0]
    n1 = int(input(f"Quanto pesa o [{n}]: "))
    l.append([n, n1])
    ca += 1
    n2 = str(input('Quer continuar [S/N] : ')).lower()[0]
    while n2 not in 'sn':
        n2 = str(input('Opçao invalida [S/N] :'))
    if n2 == 'n':
      break
co = t = ms = mn = 0
nome1 = nome2 = ''
li = []
for r in l:
    li.append(r[0])
    if co == 0:
        mn = r[1]
        ms = r[1]
        nome1 = r[0]
        nome2 = r[0]
    else:
        if r[1] < mn:
            mn = r[1]
            nome1 = r[0]
        if r[1] > ms:
            ms = r[1]
            nome2 = r[0]
    co += 1
print(li)
print(f'Ao todo voce cadastrou {ca} pessoas.')
print(f'O maior peso foi de: {ms:.2f}Kg de {nome2} ')
print(f'O menor peso digitgado foi de: {mn:.2f}Kg de {nome1}')
