from directorio.corpo.capa import *
from time import sleep
from directorio.corpo.corpoexe import *
import utilidadescev
arq = 'cadastro.txt'
if not lerarq(arq):
   criararq(arq)
while True:
    rodape('\033[37mMENU PRINCIPAL\033[m')
    menu('Ver pessoas Cadastradas', 'Cadastrar novas pessoas', 'Sair do sistema')
    n1 = leiaino('\033[37mSua opção:\033[m')
    if n1 == 1:
        rodape('\033[37mPESSOAS CADASTRADAS\033[m')
        mostrar(arq)
        linha()
    elif n1 == 2:
        rodape('\033[37mNOVO CADATRO\033[m')
        nome = str(input(' \033[37mNome: \033[m')).title().strip()
        idade = leiain(f'\033[37m{"Idade:"}\033[m')
        cadastrar(arq, nome, idade)
    else:
        if n1 == 3:
            linha()
            print(f'\033[36m{"SAINDO DO SISTEMA, ATE LOGO!":º^70}\033[m')
            linha()
            break
    sleep(0.3)
