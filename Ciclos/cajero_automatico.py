print(f'CAJERO AUTOMATICO')

# Inicializar el valor de salir
salir = False
saldo = 0

while not salir:

    print(f'''
    Menú:
        1. Depositar en cuenta
        2. Retirar de cuenta
        3. Consultar el saldo
        4. Salir
    ''')
    opcion = int(input(f'Elija una opción: '))

    if opcion == 1:
        deposito = float(input(f'Escriba la cantidad a depositar: '))
        saldo += deposito
        print(f'Has depositado en tu cuenta: ${deposito:.2f}')
        print(f'Saldo actual: ${saldo:.2f}')

    elif opcion == 2:
        retiro = float(input(f'Escriba la cantidad a retirar: '))
        if retiro > saldo:
            print(f'Saldo insuficiente')
        else:
            saldo -= retiro
            print(f'Has retirado de tu cuenta: ${retiro:.2f}')
            print(f'Saldo actual: ${saldo:.2f}')

    elif opcion == 3:
        print(f'Tu saldo actual es: ${saldo:.2f}')

    elif opcion == 4:
        print(f'Saliendo del sistema.')
        salir = True

    else:
        print(f'Elija una opción válida.')

else:
    print(f'Hasta pronto...')