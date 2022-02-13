while True:

    print(f'Analizando ordem dos parenteses')
    n = str(input('Digite uma expreçao qualquer: '))
    if n not in '()':
        print('expresao errada')