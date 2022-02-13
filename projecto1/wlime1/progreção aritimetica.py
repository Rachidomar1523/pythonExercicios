print('progreção aritimetica'.upper())
n = int(input('Qual é o primeiro termo: '))
n1 = int(input('Quantos primeiros termos queres ver: '))
n2 = int(input('Qual é a razão: '))
n3 = n+(n1-1)*n2
n4 = 0
n6 = 0
n7 = 0
r = 0
for r in range(n, n3+n2, n2):
    print(r, end='')
    print(' - ' if r < n3 else '...Mais', end='')
while n4 != 2:
    print('''
[1] Ver mais termos
[2] Sair do progrma''')
    n4 = int(input('Sua opção: '))
    n7 += 1
    if n4 == 1:
        n5 = int(input('Quantos mais termos dezejas ver: '))
        n9 = 0
        for d in range(n9, n6+n2, n2):
            if n7 < 1:
                n9 += r
            else:
                n9 += d
                n6 += n9 + (n5 - 1) * n2
            print(d, end='')
            print(' - ' if d < n6 else '...Mais', end='')
    elif n4 == 2:
        print(f'\033[31;1;4mPROGRAMA ENCERADO\033[m')
    else:
        print('\033[31;1;4mOpção invalida\033[m por favor tente novamente:')
#precizando de alguns reparus