print('progreção aritimetica'.upper())
n = int(input('Qual é o primeiro termo: '))
n1 = int(input('Quantos primeiros termos queres ver: '))
n2 = int(input('Qual é a razão: '))
n3 = 0
n4c = 1
n4f = 0
while n1 != 0:
    n3 += n1
    while n4c <= n3:
        print(f'{n}', end='')
        print(' - 'if n4c < n3 else '...mais', end='' )
        n += n2
        n4c += 1
    n1 = int(input('\nver mais termos Sua opçao: '))
if n1 == 0:
    print(f'{n1} é o {n1} primeiro termo de qualquer progreção aritimetica')
print('\033[31;1;4mPrograma encerado\033[m')
#Rever um dia