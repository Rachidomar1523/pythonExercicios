n1 = 1
while True:
    n = int(input('Digite um numero para ver a tabwada: '))
    if n < 0:
        break
    for r in range(11):
        print(f'{n} X {r} = {n * r}')
