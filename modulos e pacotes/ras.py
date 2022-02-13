
try:
    n = int(input('Digite um numero: '))
    n1 = int(input('Digite outro valor: '))
    n2 = n / n1
except ValueError:
    print('O usuario perferio nao informar os valores!')
else:
    print(f'O resultado da szua conta e igaual a:{n2} ')