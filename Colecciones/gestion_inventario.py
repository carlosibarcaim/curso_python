print(f'*** GESTION DE INVENTARIO ***')

# Inicializar la lista en donde se almacenaran los diccionarios
inventario = []
id_producto = 0
apagado = False

while not apagado:
    print(f'''Menú:
        1. Crear producto.
        2. Consultar producto por ID.
        3. Consultar todos los productos del inventario.
        4. Eliminar producto del inventario por ID.
        5. Modificar producto por ID.
        6. Salir del sistema.
    ''')
    opcion = int(input(f'Selecciona una opción del menú: '))

    if opcion == 1:

        contador = 0
        numero_productos = int(input(f'¿Cuantos productos deseas crear? '))
        while contador < numero_productos:
            id_producto += 1

            nombre_producto = input(f'Ingresa el nombre del producto: ')
            precio_producto = float(input(f'Ingresa el precio del producto: '))
            cantidad_producto = int(input(f'Ingresa la cantidad de existencias en inventario: '))

            producto = {'id': id_producto, 'nombre': nombre_producto, 'precio': precio_producto, 'cantidad': cantidad_producto}

            inventario.append(producto)

            contador += 1
            print(f'Producto(s) creado con exito!')

    if opcion == 2:
        id_consulta = int(input(f'Ingresa el ID del producto: ')) - 1

        print(f'''
            ID: {inventario[id_consulta]['id']}
            Nombre: {inventario[id_consulta]['nombre']}
            Precio: {inventario[id_consulta]['precio']:.2f}
            Cantidad: {inventario[id_consulta]['cantidad']}
        ''')

    if opcion == 3:
        print(f'Todos los productos: ')
        for producto in inventario:
            for llave, valor in producto.items():
                print(f'''{llave}: {valor}''')

    if opcion == 4:
        id_eliminar = int(input(f'Ingresa el ID del producto que deseas eliminar: ')) - 1
        del inventario[id_eliminar]
        print(f'Producto eliminado.')

    if opcion == 5:
        id_modificar = int(input(f'Ingresa el ID del producto que deseas modificar: ')) - 1
        nombre_producto = input(f'Ingresa el nombre del producto: ')
        precio_producto = float(input(f'Ingresa el precio del producto: '))
        cantidad_producto = int(input(f'Ingresa la cantidad de existencias en inventario: '))
        del inventario[id_modificar]
        producto = {'id': id_modificar + 1, 'nombre': nombre_producto, 'precio': precio_producto, 'cantidad': cantidad_producto}
        inventario.append(producto)
        print(f'Producto Modificado con exito!')

    if opcion == 6:
        print(f'Saliendo del sistema...')
        apagado = True