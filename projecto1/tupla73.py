n = 'rachid', 'Omar', 'Merson', 'Govanhica', 'Delfim', 'Mario', 'Pedro', 'joaquim', 'Mulangua','vicente'
n3 = int(input('Quantos primeiros queres ver: '))
n2p = int(input('quantos ultimos queres ver: '))
n1 = len(n) - n2p
n2 = n[:n3]
print(f'''Todos os nomes da lista sao: [{n}]
Os {n3} primeiros sao: {n2}
Os {n2p} ultimos sao: {n[n1:]}''')

