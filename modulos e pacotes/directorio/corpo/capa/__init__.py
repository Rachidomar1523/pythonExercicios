from utilidadescev import *


def linha(n=70):
    print('\033[37m-\033[m'*n)


def centrar(n='', a=0, b=''):
    return f'\033[37m|\033[m {n:{b}^{a}} \033[37m|\033[m'


def rodape(n=''):
    linha()
    print(centrar(n, 74))
    linha()


def menu(*n):
    cont = 0
    for c in n:
        cont += 1
        print(f'\033[37m|\033[m \033[30m{cont} - \033[37m{c:<62} \033[37m|\033[m \033[30m')
    linha()
