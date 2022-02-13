n = float(input('Digite o 1º numero: '))
n1 = float(input('Digite o 2º numero: '))
n2 = 0
while n2 != 5:
    print('''  [1] somar
  [2] Multiplicar
  [3] Maior
  [4] Novos numeros
  [5] Sair do programa''')
    n2 = int(input('Sua opção: '))
    if n2 == 1:
        n3 = n + n1
        print(f'A soma entre {n} + {n1} é igual a {n3}')
    elif n2 == 2:
        n4 = n * n1
        print(f'O produto de {n} x {n1} é igual a {n4}')
    elif n2 == 3:
        if n > n1:
            print(f'O maior numero digitado foi {n}')
        else:
            print(f'O maior numero digitado foi {n1}')
    elif n2 == 4:
        n7 = float(input('Digite o 1º numero: '))
        n8 = float(input('Digite o 2º numero: '))
        n = n7
        n1 = n8
    elif n2 == 5:
        print('\033[1;4;31mFINALIZANDO O PROGHRAMA!\033[m')
    else:
        print('\033[1;4;31mOpção invalida\033[m por favor digite novamente: ')