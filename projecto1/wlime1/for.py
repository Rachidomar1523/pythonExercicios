n0 = 0
n01 = 0
n3 = 0
n4 = ''
n5 = 0
n6 = 0
for r in range(1, 4):
    print(f'_____ {r}ªpessoa ________')
    n = str(input(f' Nome: ')).title()
    n1 = int(input(f'Idade: '))
    n2 = str(input(f'Sexo [M/F]: ')).capitalize()
    n0 += n1
    n01 = n0 / r
    if n2 in 'Mm' or 'Masculino' and r == 1:
        n3 = n1
        n4 = n
    if n2 in 'Mm' and n1 > n3:
        n3 = n1
        n4 = n
    if n2 in 'Mm':
        n6 += 1
    if n2 in 'Ff':
        n5 += 1
print(f'A media das idades foi: \033[1;36m{n01:.2f}\033[m anos')
print(f'O homen mais velho tem \033[31;1m{n3}\033[m anos e chama se \033[32;1m{n4}\033[m')
print(f'Num grupo tem ao todo \033[35;1m{n5}\033[m mulheres e \033[33;1m{n6}\033[m homens')