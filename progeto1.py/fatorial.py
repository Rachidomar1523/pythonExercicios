n2 = 0
print('Factorial de um numero!')
n = int(input('Digite um numero para ver o seu factorial: '))
print(f'''[1] Ver factorial de {n}!
[2] Digitar novo numero
[3] Sair do programa''')
n1 = int(input('\033[1;37mSua opção:\033[m '))
if n1 == 1:
    n4 = 1
    for c in range(n, 0, -1):
        print(f'{c}', end='')
        print(' X ' if c > 1 else ' = ', end='')
        n4 *= c
    print(f'{n4}')
n5 = 1
if n1 == 2:
    n = int(input('Digite o novo valor: '))
    for c in range(n, 0, -1):
        print(f'{c}', end='')
        print(' X ' if c > 1 else ' = ', end='')
        n5 *= c
    print(n5)
if n1 != 1 != n1 != 2 != n1 != 3:
    print('Opção invalida digite novamente \033[31;1m1; 2 ou 3\033[m:')
while n2 != 2:
    print(f'''[1] Digitar novo numero
[2] Sair do programa''')
    n2 = int(input('\033[1;37mSua opção:\033[m '))
    n6 = 1
    if n2 == 1:
        n = int(input('Digite o novo valor: '))
        for c in range(n, 0, -1):
            print(f'{c}', end='')
            print(' X ' if c > 1 else ' = ', end='')
            n6 *= c
        print(n6)
    elif n2 == 2:
        print('Encerando...')
    else:
        print('Opção invalida tente novamente:')
print('\033[31;1;4mPROGRAMA ENCERADO!\033[m')