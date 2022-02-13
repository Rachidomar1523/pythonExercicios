def aumentar(num=0, taxa=10, formata=False):
    s = num + ((num * taxa) / 100)
    return s if formata is False else formatar(s)


def diminuir(num=0, taxa=10, formata=False):
    s = num - ((num * taxa) / 100)
    return s if formata is False else formatar(s)


def metade(num=0, formata=False):
    s = num / 2
    return s if formata is False else formatar(s)


def dobro(num=0, formata=False):
    s = num * 2
    return s if formata is False else formatar(s)


def formatar(num=0):
    s = f'{f"{num:.2f}"}'.replace('.', ',')
    return s


def resumo(p, a, d):
    print('_' * 30)
    print(f"{'ESUMO DO VALOR':_^30}")
    print(f'''{"Preço analizado:":<20}{formatar(p):^10}
{"Dobro do Preço :":<20}{f"{dobro(p, True)}":^10}
{"Metade do preço:":<20}{f"{metade(p, True)}":^10}
{f"{a}% de aumento :":<20}{f"{aumentar(p, a, True)}":^10}
{f"{d}% de reduçao :":20}{f"{diminuir(p, d, True)}":^10}''')
    print('_' * 30)

