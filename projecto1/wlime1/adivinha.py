import random
n1 = random.randint(0, 10)
print(n1)
n3 = int(input('Tente adivinlhar Qual numero estou pensando: '))
n2 = 1
while n3 != n1:
    n1 = random.randint(0, 10)
    print(n1)
    n3 = int(input('\033[31;1mPerdeste\033[m tente de novo em que numero estou pensando: '))
    n2 += 1
print(f'\033[1;36mPARABENS\033[m tu ganhaste MAIS precizaste de \033[34;1;4m{n2}\033[m tentativas para me vencer')

