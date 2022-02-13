import moeda
p = float(input('Digite o preço: '))
print(f'A metade de {moeda.formatar(p)} Mt é: {moeda.metade(p,True)} Mt')
print(f'O dobro de {moeda.formatar(p)} Mt é: {moeda.dobro(p, True)} Mt')
print(f'aumentando 10% temos: {moeda.aumentar(p,10, True)} Mt')
print(f'Diminuindo 13% temos: {moeda.diminuir(p, 1, True)} Mt')