n = int(input('Quantos primeiros termos FIBONACCI queres ver: '))
n1 = 0
n2 = 1
n4 = 3
print(f'{n1} - {n2} - ', end='')
while n4 <= n:
      n4 += 1
      n3 = n1 + n2
      n1 = n2
      n2 = n3
      print(f'- {n3} - ', end='')
print('mais')