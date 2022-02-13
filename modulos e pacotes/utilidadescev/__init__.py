def leiain(a='Digite um numero inteiro'):
    c = 0
    n2 = 0
    while True:
        try:
            n = input(f' {a.strip()} ').strip()
            n1 = n.isnumeric()
            if n1:
                n2 = int(n)
                break
            else:
                print('\033[31;1mERRO! digite um numero inteiro valido.\033[m')
                c += 1
        except:
            print('\033[31;1mERRO! por favor digite um valor valido.\033[m')
        if c >= 2:
            break
    return n2


def leiaino(a='Digite um numero inteiro', b='Digite um numero real'):
    c = 0
    n2 = 0
    c1 = 0
    while True:
        try:
            n = input(f' {a.strip()} ').strip()
            n1 = n.isnumeric()
            if n1:
                n2 = int(n)
                if n2 <= 3:
                    break
                else:
                    print('\033[31m ERRO! Digite uma opção valida.\033[m')
                    c1 += 1
            else:
                print('\033[31m ERRO! digite um numero inteiro valido.\033[m')
                c += 1
        except:
            print('\033[31;1mERRO! por favor digite um valor valido.\033[m')
        if c >= 2 or c1 >= 2:
            break
    return n2