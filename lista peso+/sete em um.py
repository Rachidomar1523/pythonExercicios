c = 1
l = [[], []]
for r in range(0, 5):
    n = int(input(f'digite o {c}ª numero: '))
    if n % 2 == 0:
        l[0].append(n)
    else:
        if n % 2 != 0:
            l[1].append(n)
    c += 1
l[0].sort()
l[1].sort()
print(f'so os inpares sao:{l[1]} '
      f'e so os pares: {l[0]}')
