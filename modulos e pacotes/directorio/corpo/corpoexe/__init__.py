def lerarq(arquivo):
    try:
        a = open(arquivo, 'rt')
        try:
            a.close()
        except:
            print(f'\033[31mProblema ao o fechar o arquivo \033[m')
    except:
        return False
    else:
        return True


def criararq(arquivo):
    try:
        a = open(arquivo, 'wt+')
    except:
        print('\033[31mProblema nam criação do arquivo\033[m')
    else:
        print(f'\033[32mArquivo {arquivo} criado com sucesso!\033[m')


def mostrar(arquivo):
    try:
        a = open(arquivo, 'rt')
    except:
        print(f'\033[31mArquivo {arquivo} não encontrado\033[m')
    else:
       try:
           l = []
           for r in a:
               l.append(r.replace('\n', '').split(';'))
               l.sort()
       except:
           print('\033[31mProblema encontrado!\033[m')
       else:
           for v in l:
               print(f'\033[37m|\033[m {v[0]:<53}{v[1]:>8} anos \033[37m|\033[m')
       finally:
           a.close()


def cadastrar(arquivo, nome='DESCONLHECIDO', idade=0):
    try:
        a = open(arquivo, 'at')
    except:
        print('\033[31mArquivo não encontrado!\033[m')
    else:
        try:
            a.write(f'{nome};{idade}\n')
        except:
            print('Problema ao cadastrar')
        else:
            print(f'\033[32m"{nome}" cadastrsdo com sucesso!\033[m')
        finally:
            a.close()

