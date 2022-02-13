n0 = int(input('Quantos numeros queres analizar: '))
n0c = nc = n1 = n1c = r = n= 0
while n1 != 2:
    n0c += 1
    for r in range(n0):
        n = float(input(f'Digite o {n1c+1}º numero: '))
        n1c += 1
        nc += n
    print('''    [1] Digitar mais numeros
    [2] Analizar
     
    [3] Sair do programa''')
    n1 = int(input('Sua opção: '))
    if n1 == 1:
        n0 = int(input('Quantos numeros mais queres digitar: '))
    elif n1 == 2:
         print(f'''  Numeros digitados: {n1c:>10}
  A soma entre eles: {nc:>10}''')
    elif n1 == 3:
        print('\033[1;4;31mPROGRAMA ENCERADO!\033[m')
        break
    else:
        print('\033[1;31;4mopção invalida\033[m por favor digite novamente')

