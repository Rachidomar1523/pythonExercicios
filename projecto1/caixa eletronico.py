print('Notas disponiveis: [50R$;20R$;10R$;1R$]')
sacar = int(input('Quanto queres sacar do caixa eletronico ["0" para sair]: '))
saca = sacar
cedula = 50
contador = 0
while True:
    if saca >= cedula:
        saca -= cedula
        contador += 1
    else:
        if contador > 0:
            print(f'Total de {contador} cedulas de {cedula}R$')
        if cedula == 50:
            cedula = 20
        elif cedula == 20:
             cedula = 10
        elif cedula == 10:
            cedula = 1
        contador = 0
        if saca == 0:
            break