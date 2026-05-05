print(f'*** APLICACION CALCULADORA ***')

salir = False

while not salir:
    print(f'''
        Calculadora:
        
        1. Suma
        2. Resta
        3. Multiplicación
        4. División
        5. Salir
    ''')

    opcion = int(input(f'Elige una de las opciones de la calculadora: '))

    if opcion == 1:
        operando1 = float(input(f'Ingrese el primer numero: '))
        operando2 = float(input(f'Ingrese el segundo numero: '))
        resultado = operando1 + operando2
        print(f'El resultado de la suma es: {resultado}')

    elif opcion == 2:
        operando1 = float(input(f'Ingrese el primer numero: '))
        operando2 = float(input(f'Ingrese el segundo numero: '))
        resultado = operando1 - operando2
        print(f'El resultado de la resta es: {resultado}')

    elif opcion == 3:
        operando1 = float(input(f'Ingrese el primer numero: '))
        operando2 = float(input(f'Ingrese el segundo numero: '))
        resultado = operando1 * operando2
        print(f'El resultado de la multiplicación es: {resultado}')

    elif opcion == 4:
        operando1 = float(input(f'Ingrese el primer numero: '))
        operando2 = float(input(f'Ingrese el segundo numero: '))
        resultado = operando1 / operando2
        print(f'El resultado de la división es: {resultado}')

    elif opcion == 5:
        print(f'Saliendo de calculadora...')
        salir = True

    else:
        print(f'Elija una opción valida')

else:
    print(f'Hasta pronto...')