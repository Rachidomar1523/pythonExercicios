n1 = []
cont = mais = entre = menos = 0
for c in range(5):
    cont += 1
    n = int(input(f'digite um valor para a posiçao {c}: '))
    if cont == 1:
        mais = n
        menos = n
        print('Numero digitado ao fim da lista!0')
    else:
        if n > mais:
            mais = n
            n1.insert(4, n)
            print('valor digitado na posiçao  fim da lista 4')
        else:
            if n == mais:
                n1.insert(3, n)
                print('Numero digitado oa fim da lista!3')
        if n < menos:
            menos = n
            n1.insert(0, n)
            print('Valor adicionado nam posiçao 0')
        else:
                if n == menos:
                    n1.insert(1, n)
                    print('Valor adicionado nam posiçao 1')
print(n1)

