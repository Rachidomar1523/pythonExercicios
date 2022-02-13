print('''as tuplas sao imutaveis esta e a diferença basica das tuplas com as listas
para nos substituirmos valores dentro de uma lista basta so EX: n = ["Rachid","Omar", "Merson", "Govanhica"]
n[1] = "Messo" logo o conputador vai substituir o omar por Messo  ja que o omar e o numero 1 da listalogo o
"n" vai ser igual a: ["Rachid","Messo", "Merson", "Govanhica"] mais esta forma nao funciona para adicionarmos elementos a lista
logo deve se usar outra tecnica : que é a funçao append() EX: n.append(dchira) ele vai colocar num final a palavra dchira logo
o "n" vai ser iqual a: ["Rachid","Omar", "Merson", "Govanhica","Dchira"] a funçao append() e so para colocar caracteres num final
da lista para colocar caracteres num entre outros usa se o objecto de listga clhamado "inset()" EX: n.insert(0,carro) ele nai colocar
a palavra carro na possiçao "0" que era antes o nome rachid logo fica n = ["Carro", "Rachid","Omar", "Merson", "Govanhica"]
Tanbem nas listas pode se eliminar elementos com os comandos "del; EX: del n[3]", "pop; EX: n.pop(3) normalmente o comando pop e para
eliminar o ultimo elemento mais pode se tanbem indicar o parametro como o EXenplo de cima ilustra nb: o numero tres e o indes(a posiçao)"
"remove() o comando remove() voce nao indica o indes(posiçao) mais o valor (o que esta na posiçao) EX: n.remove('Rachid')"
quando se tenta remover elementos que nao estao na lista vai se receber um erro da linguagem existe uma forma de fazer melhor isso
que usando as estruturas condicionais; EX: if rachid in n: n.remove('Rachid')
podemos tanbem criar uma lista usando o comando range(); EX: n1 = list(rang(4, 11)) ele vai criar uma lista de 4 a 11 ordenados de forma crescente
o comand sort ele ordena as coisas de forma crescente, EX: n2 = [5, 4, 3, 2, 1, 0],n2.sort() ele vai ordenar os numeros de forma crescente e vai ficar
[0, 1, 2, 3, 4, 5] pode se tanbem ordenalos de na forma decrescente utilizando o metodo n2.sort(reverse=True) se quisermos saber o tamanho da lista
podemos usar ocomando interno do python o comando len(n2)''')
#n = [2, 3, 5, 1, 4, 8, 4])
#print(n)
#n.append(10)
#n.sort(reverse=True)
#n.insert(4, 20)
#print(n)
n1 = []
for c in range(5):
    n1.append(int(input('digite um valor: ')))
for d,r in enumerate(n1):
   print(f'Nam posiçao {d} encontrei {r}')
print('Lista terminada!')
print('Os valores organizados seria:')
n1.sort()
for h, i in enumerate(n1):
    print(f'Nam posiçao {h} encontrei {i}')