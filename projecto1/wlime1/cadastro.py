p = h = m = 0
while True:
    n = int(input('Quantos anos tens: '))
    n1 = str(input('De que sexo tu es [F/M]: ')).strip().upper()[0]
    while n1 not in 'FM':
        n1 = str(input('Opção invalida por favor informe seu sexo [F/M]: ')).strip().upper()[0]
    print('*' * 39)
    n2 = str(input('Quer continuar cadastrando [S/N]: ')).strip().upper()[0]
    while n2 not in 'SN':
        n2 = str(input('Opçao invalida.informe se querer continuar cadastrsndo [S/N]: ')).strip().upper()[0]
    print('*'*39)
    if n > 18:
        p += 1
    if n1 == 'M':
        h += 1
    if n1 == 'F' and n < 20:
        m += 1
    if n2 == 'N':
        break
print('<x>'*20)
print(f'''    Pessoas maiores de 18 anos                     :    \033[37;1;4m{p}\033[m            
    Total de homens cadastrados                    :    \033[31;1;4m{h}\033[m
    Total de mulheres cadastradas menos de 20 anos :    \033[36;1;4m{m}\033[m''')
print('<x>'*20)