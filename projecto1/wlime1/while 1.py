n = str(input('informe o seu genero [M/F]: ')).strip().upper()[0]
while n not in 'MmfF':
    n = input('genero invalido por favor digite um genero valido [M/F]').strip().upper()[0]
    if n == 'M':
        print('genero MASCULINO registado com sucesso')
    elif n == 'F':
        print('genero feminino registado com sucesso')
