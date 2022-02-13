print('='*40)
print(f'{"Banco Rachid":>^40}')
print('='*40)
n = int(input('Sacar[Notas desponiveisR$ 50;20;10;1]: '))
nc1 = n
nc = 0
nco = 50
while True:
    if nc1 >= nco:
        nc1 -= nco
        nc += 1
    else:
        if nc > 0:
            print(f'Total de {nc} cedulas de {nco}Mt')
        if nco == 50:
            nco = 20
        elif nco == 20:
            nco = 10
        elif nco == 10:
            nco = 1
        nc = 0
        if nc1 == 0:
            break
