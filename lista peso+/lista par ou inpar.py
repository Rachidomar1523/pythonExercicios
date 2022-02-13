n1 = list()
n2 = []
n3 = []
n = 0
while True:
    n = int(input('Digite um numero: '))
    n1.append(n)
    nq = str(input('Queres continuar: ')).upper()
    while nq not in 'NS':
        nq = str(input('Opçao invalida [S/N]:')).upper()
    if n % 2 == 0 and n != 0:
        n2.append(n)
    if n % 2 != 0 or n == 0:
        n3.append(n)
    if nq == 'N':
        break
print(f'os valores digitados forão: {n1}')
print(f'Os valores pares digitados forão: {n2}')
print(f'Os valores inpar digitados forão: {n3}')
