print('Bem vindo ao jogo de par ou inpar')
import random
nc = random.randint(0, 10)
np = int(input('Digite um numero de \033[1;37m[0 - 10]\033[m: '))
npi = str(input('Par ou Inpar: ')).upper()
rs = nc + np
n1 = 0
while True:
    if npi in 'PI':
        break
    n1 = random.randint(30, 37)
    npi = str(input(f'\033[31;1mOpçao invalida\033[m por favor digite \033[{n1};4;1m[PAR ou INPAR]\033[m: ')).upper()
if npi == 'P' and rs % 2 != 0:
        n1c = 0
        while True:
            nc = random.randint(0, 10)
            npi = str(input(f'''voce escolheu "{np}" e o conputador escolheo "{nc}" e entao {np} + {nc} = {rs}
o resto da divisão de {rs} por 2 é diferente de 0 por tanto é inpar "{rs % 2:.0f}" perdeste! 
por favor digite \033[{n1};4;1m[PAR ou INPAR]\033[m: ''')).upper()
            n1c += 1
            if npi in 'PI':
                break
if npi == 'P' and rs % 2 == 0:
    n2c = 0
    while True:
         print(f'''\033[1;36;4mPARABENS GANHASTE\033[m o conputador escolheu {nc} voçe escolheu {np}
{nc} + {np} = {rs} o resto da divisão de {rs} por 2 e igual há "{rs % 2:.0f}" por isso é par''')
         if rs % 2 == 0:
            break
         n2c += 1
if npi == 'P' and rs % 2 != 0:
    n3c = 0
    while True:
        nc = random.randint(0, 10)
        npi = str(input(f'''voce escolheu "{np}" e o conputador escolheo "{nc}" e entao {np} + {nc} = {rs}
o resto da divisão de {rs} por 2 é diferente de 0 por tanto é inpar "{rs % 2:.0f}" perdeste! 
por favor digite \033[{n1};4;1m[PAR ou INPAR]\033[m: ''')).upper()
        if npi in 'PI':
            break
        n3c += 1
if npi == 'I' and rs % 2 != 0:
    n4c = 0
    while True:
        nc = random.randint(0, 10)
        print(f'''\033[1;36;4mParabens ganhaste\033[m o conputador escolheu {nc} voçe escolheu {np}
{nc} + {np} = {rs} o resto da divisão de {rs} por 2 é igual há "{rs % 2:.0f}" por isso é inpar''')
        if rs % 2 != 0:
            break
        n4c += 1
if npi == 'I' and rs % 2 == 0:
    n5c = 0
    while True:
        nc = random.randint(0, 10)
        npi = str(input(f'''voce escolheu "{np}" e o conputador escolheo "{nc}" e entao {np} + {nc} = {rs}
o resto da divisão de {rs} por 2 é diferente de 0 por tanto é inpar "{rs % 2:.0f}" perdeste! 
por favor digite \033[{n1};4;1m[PAR ou INPAR]\033[m: ''')).upper()
        if npi in 'PI':
            break
        n5c += 1

print('                         \033[31;1;4mPROGRAMA ENCERADO!\033[m')
