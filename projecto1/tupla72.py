n1 = 'zero', 'Um', 'Dois', 'Tres', 'Quatro', 'Cinco', 'Seis', 'Cete', 'Oito', 'Nove', 'Dez', 'Onze', 'Doze', 'Treze', 'Catorze', 'Quinze', 'Desaseis', 'Desacete', 'Dezoito', 'Dezanove', 'Vinte'
nes = int(input('Digite um numero: '))
parada = 0
while True:
    if parada == 2:
        break
    while True:
        if 0 <= nes >= 20:
            break
        nes = int(input('opçao invalida por favor Digite um numero de [0-20]: '))
    print(f'Eu digitei o numero \033[1;4;34m{n1[nes]}\033[m')
    print('''    [1] continuar
    [2] Sair do programa''')
    parada = int(input('sua opçao: '))
    if parada == 1:
        nes = int(input('Digite um numero: '))