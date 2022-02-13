def leiain(a='Digite um numero inteiro', b='Digite um numero real'):
    while True:
        n = input(f'{a}: ').strip()
        n1 = n.isnumeric()
        if n1:
            n2 = int(n)
            break
        else:
            print('\033[31;1mERRO! digite um numero inteiro valido.\033[m')
    while True:
        n0 = input(f'{b}: ').strip().replace(',', '.')
        n01 = n.isalpha()
        if not n01:
            if '.' in n0:
                n02 = float(n0)
                break
            else:
                print('\033[31;1mERRO! digite um numero real valido.\033[m')

        else:
            print('\033[31;1mERRO! digite um numero real valido.\033[m')
    return n2, n02


n = leiain()
print(f'Voçe digitou numero inteiro: {n[0]} e numero real {n[1]}')