maior = cont = pos = posm = menor = 0
l = []
for c in range(5):
    l.append(int(input(f'Digite um numero para  posiçao {c}: ')))
for p in l:
    cont += 1
    if cont == 1:
        maior = p
    else:
        if p > maior:
            maior = p
            for en, po in enumerate(l):
                if po == maior:
                    pos = en
    if cont == 1:
        menor = p
    else:
         if p < menor:
            menor = p
            for enu, posi in enumerate(l):
                if posi == menor:
                   posm = enu
print(f'''valores digitados: {l}
o maior numero digitado foi {maior} na posiçao {pos}
E o menor numero digitado foi: {menor} na posiçao {posm}''')