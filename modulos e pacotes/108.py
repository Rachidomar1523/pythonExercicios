import moeda
p = float(input('Digite o preço: '))
print(f'A metade de {moeda.formatar(p)} Mt é: {moeda.formatar(moeda.metade(p))} Mt')
print(f'O dobro de {moeda.formatar(p)} Mt é: {moeda.formatar(moeda.dobro(p))} Mt')
print(f'aumentando 10% temos: {moeda.formatar(moeda.aumentar(p))} Mt')
print(f'Diminuindo 13% temos: {moeda.formatar(moeda.diminuir(p))} Mt')