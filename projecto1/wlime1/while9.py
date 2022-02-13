n1c = n = n1 = 0
n = float(input(f'digite o numero: '))
while n != 999:
     n1c += 1
     n1 += n
     n = float(input(f'digite o {n1c}º numero: '))
print(f'Voçe digito {n1c} numeros e a soma entre eles é igual a {n1}')