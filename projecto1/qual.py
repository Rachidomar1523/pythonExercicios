n = ''
n1 = []
c = cont = v = 0
while n != 'N':
    n2 = int(input('Digite um numero: '))
    n1.append(n2)
    c += 1
    for d, i in enumerate(n1):
          if i == 5:
            cont += 1
            v = d
    n = str(input(f'Quer continuar: ')).upper()[0]
n1.sort()
print(f'Total, de numeros digitados {c} que sao os sequintes {n1}')
print(f'Ordenados de forma crescente {n1}')
n1.sort(reverse=True)
print(f'E ordenados de forma decrescente: {n1}')
if cont != 0:
    print(f'O valor cinco (5) esta na lista assumindo a posiçao: {cont}', "vezes" if cont == 1 else\
        "vezes", f'nas posiçoes {v}' if cont > 1 else f'na posiçao {v}')
else:
    print(f'O valor cinco (5) nao esta na lista')
