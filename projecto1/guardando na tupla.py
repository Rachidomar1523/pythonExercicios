n = 'Lapis', 1.75, 'Borracha', 2.0, 'caderno', 15.90, \
    'Estojo', 25.0,'Transferidor', 4.20, 'Compaço', 9.99, \
    'Mochila', 120.32, 'Caderno', 22.30, 'Livro', 34.90
print('='*45)
print(f'{"Listagem de preços":<^40}')
print('='*45)
for r in range(0, len(n)):
    if r % 2 == 0:
        print(f'{n[r]:.<30}', end='')
    else:
        print(f'R$ {n[r]:>7.2f}')
print('='*45)
print(len(n))
# OU ESTE EM BAIXO
n = 'carro', 250, 'bisicleta', 54, 'mota', 60, 'portoaviao', 100
c = 0
print('='*40)
print(f'{"Listagem de preço":<^40}')
print('='*40)
for r in n:
    c += 1
    if c % 2 != 0:
        print(f'{n[c-1]:.<30}', end='')
    else:
        print(f'R${n[c-1]:>7}')
print('='*40)