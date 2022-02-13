n = 'rachid', 'Omar', 'merson', 'Govanlhica'
for r in n:
    print(f'\nNam palavra {r} temos: ', end='')
    for p in r:
        if p.lower() in 'aeiou':
            print(p, end=' ')
