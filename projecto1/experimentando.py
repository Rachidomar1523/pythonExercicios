c = nc0 = menor = nc = 0
nome = ''
while True:
    n0 = str(input('Qual e o nome do produto: '))
    n = int(input('Quanto custa: '))
    n1 = str(input('Queres continuar: ')).upper()[0]
    if n1 not in 'NS':
        while True:
            n1 = str(input('Opçao invalida: ')).upper()
            if n1 in 'NS':
               break
    nc0 += n
    if n > 100:
        nc += 1
    c += 1
    if c == 1:
      menor = n
      nome = n0
    else:
        if n < menor:
            menor = n
            nome = n0
    if n1 == 'N':
        break
print(f'''{"Total gasto":-<30}R$ {nc0:<7.2f}Mt
{"Custando mais de mil":-<30} {nc} {"produtos":<7}
 {"Produto mais barato":-<30}{nome}''')
