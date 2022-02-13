def leiadinheiro(a='Digite um valor:'):
    while True:
        n1 = str(input(f'{a} ')).replace(',', '.')
        n2 = n1.isalpha()
        if n1.isalpha() or n1 == '':
            print(f'\033[31;1mERRO!, "{n1}" é um valor invalido.\033[m ')
        else:
            n1 = float(n1)
            break
    return n1
