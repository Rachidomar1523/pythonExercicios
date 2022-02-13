'''nc = 0
n1 = n2 = n3 = n4 = nt1 = nt2 = nt = n5 = 0
while True:
    nc += 1
    n = int(input('Digite um numero: '))
    if nc == 1:
        n1 = n
    else:
        if nc == 2:
            n2 = n
        elif nc == 3:
                n3 = n
        elif nc == 4:
            n4 = n
        elif nc == 5:
            n5 = n
    nt = n1, n2, n3, n4, n5
    if nc == 5:
        break
    print(nt if n % 2 == 0 else 'nao existe nenhum numero par digitado')
if nt.count(9) > 1:
    nv = 'vezes'
else:
    nv = 'vez'
print(f'''#O numero 9 {f"foi digitado {nt.count(9)} {nv}"if nt.count(9) > 0 else " nao foi digitado!" }
#O primeiro numero 3 foi digitado na posiçao: {nv.find('3')}
#Numeros pares {nt}''')'''
# para verificar quando tiver megas!
# ESta foi a soluçao do professor / A de cima foi minlha e tem algumas falhas "rachid verifique depois"
# nb: memorizarf o metodo de baixo do professor
n0 = (int(input('Digite um numero: ')),
      int(input('Digite um numero: ')),
      int(input('Digite um numero: ')),
      int(input('Digite um numero: ')))
print(f'''O valor 9 apareceu {n0.count(9)} vez
{"O primeiro valor 3 aparece nam posiçao {}" if 3 in n0 else "nao foi digitado nunhu valor 3"}''')
print(f'Valores pares digitados sao: ', end='')
for n in n0:
    if n % 2 == 0:
        print(n, end=" ")
