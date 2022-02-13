n1c = n2c = n3c = mc = nc = 0
n2 = ''
while n2 in 'Nn':
    n1c += 1
    n = int(input(f'Digite o {n1c}º numero: '))
    n2 = str(input('voçe quer continuar digitando [S/N]: ')).capitalize()
    n2c += n
    n3c = n2c / n1c
    if n1c == 1:
      mc = n
      nc = n
    elif n > mc:
        mc = n
    elif n < nc:
        nc = n
print(f'''\033[37;4;1m                                            \033[m
    Numeros digitados      :    \033[1;4;34m{n1c:}\033[m
    Media dos numeros      :    \033[1;31;4m{n3c:.1f}\033[m
    Maior numero digitado  :    \033[1;4;36m{mc}\033[m
    Nenor numero digitgado :    \033[1;4;32m{nc}\033[m
\033[37;4;1m                                            \033[m''')
print(f'           \033[1;35;4m PROGRAMA ENCERADO! \033[m')
# rever