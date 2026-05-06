# Pograma para introducir y mostrar Receta de cocina

print('*** Recetas ***')
print('A continuación ingrese los datos de la receta\n')

# Pedir al usuario ingresar los datos de la receta
nombre_receta = input('Ingresa el nombre de la receta: ')
ingredientes = input('Ingresa el nombre de los ingredientes: ')
tiempo_preparacion = float(input('Ingresa el tiempo de preparacion en minutos: '))
dificultad_receta = input('Ingresa la dificultad de la receta (Facil, Media, Alta)')

# Imprimir los datos en consola
print(f'''
    Nombre de la receta: {nombre_receta}
    Ingredientes: {ingredientes}
    Tiempo de preparación: {tiempo_preparacion} minutos
    Dificultad de preparación: {dificultad_receta}
''')