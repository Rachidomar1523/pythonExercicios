nt = nc = m = n6 = pmais = pmenos = 0
nmais = n = nmenos = m1 = ''
while True:
    nome = str(input('Qual e o nome do produto: '))
    n1 = float(input('Quanto custa: '))
    nt += n1
    nc += 1
    print('<x>x'*10)
    n2 = input('Quer continuar conprando [S/N]: ').strip().upper()[0]
    while n2 not in 'SN':
        n2 = input('opção invalida por favor infom se Queres continuar conprando [S/N]: ').strip().upper()[0]
    print('<x>x' * 10)
    if nc == 1:
        nmais = nome
        nmenos = nome
        pmais = n1
        pmenos = n1
    if n1 > pmais:
        pmais = n1
        nmais = nome
    if n1 < pmenos:
        pmenos = n1
        nmenos = nome
    if n1 > 1000:
        m += 1
    if m <= 0:
        m1 = 'Não ha Nenhum'
    else:
        m1 = m
    if n2 == 'N':
        print('         \033[31;1;4mPROGRAMA ENCERADO!\033[m')
        print(f'''<x>x<x>x<x>x<x>x<x>x<x>x<x>x<x>x<x>x<x>x<x>x<x>x<x>x<x>x<x>x<x>x<x>x<x>x<x>x<x>x<x><x>
    Total gasto                      :    num total da conpra gastou se {nt}Mt
    Produto custando mais de 1000 Mt :    {m1} produtos custando mais de 1000Mt
    Nome do produto mais barato      :    {nmenos} custando {pmenos}Mt 
    Produto mais carro               :    {nmais} custando {pmais}Mt
<x>x<x>x<x>x<x>x<x>x<x>x<x>x<x>x<x>x<x>x<x>x<x>x<x>x<x>x<x>x<x>x<x>x<x>x<x>x<x>x<x><x>''')
        break

