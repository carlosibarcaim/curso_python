print(f'MENU ITERATIVO')

# Inicializar la variable salir
salir = False

# Iterar y mostrar mensajes
while not salir:

    # Imprimir en consola las opciones
    print(f'''
    Menu:
        1. Crar cuenta
        2. Eliminar cuenta
        3. Salir
    ''')

    # Pedir al usuario que elija una opción
    opcion_elegida = int(input(f'Elije una opción del menú: '))

    # Mostrar mensaje dependiendo de la opción elegida
    if opcion_elegida == 1:
        print(f'Creando cuenta...')
    elif opcion_elegida == 2:
        print(f'Eliminando cuenta...')
    elif opcion_elegida == 3:
        print(f'Saliendo del sistema')
        salir = True
    else:
        print(f'Elija una opción valida')