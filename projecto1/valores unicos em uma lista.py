l = []
cont = 0
while True:
    n = int(input(f'Digite um valor na posiçao {cont}: '))
    cont += 1
    if n not in l:
        l.append(n)
        print('Valor adicionado com sucesso')
    else:
        print('valor dupllicado nao vou adicionaor: ')
    n = str(input('Quer continuar: ')).upper()[0]
    if n in 'Nn':
        break
l.sort()
print(l)
