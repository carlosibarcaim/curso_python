print(f'*** LISTA DE SUSCRIPTORES ***')

# Crear la lista de suscriptores
lista_suscriptores = set()

apagado = False

while not apagado:
    print(f'''
    Menu: 
        1. Agregar suscriptor
        2. Eliminar suscriptor
        3. Consultar lista de suscriotores
        4. Salir del sistema
    ''')

    opcion = int(input(f'Elige una opción: '))

    if opcion == 1:
        agregar_email = input(f'Ingresa tu email con el que deseas ingresar: ').strip().lower()
        if agregar_email in lista_suscriptores:
            print(f'Ya existe el email {agregar_email} en la lista de suscriptores.')
        elif agregar_email not in lista_suscriptores:
            lista_suscriptores.add(agregar_email)
            print(f'Suscriptor "{agregar_email}" agregado con exito!')

    if opcion == 2:
        eliminar_email = input(f'Ingresa el email que deseas eliminar: ').strip().lower()
        if eliminar_email not in lista_suscriptores:
            print(f'No existe el email {eliminar_email} en la lista de suscriptores.')
        elif eliminar_email in lista_suscriptores:
            lista_suscriptores.remove(eliminar_email)
            print(f'Suscriptor "{eliminar_email}" eliminado con exito!')

    if opcion == 3:
        print(f'Lista de suscriptores: ')
        for suscriptor in lista_suscriptores:
            print(suscriptor)

    if opcion == 4:
        print(f'Saliendo del sistema... Vuelva pronto')
        apagado = True
