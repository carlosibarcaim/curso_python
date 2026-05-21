print(f'*** Función con argumentos por nombe ***')

def imprimir_nombre(nombre, apellido= '', edad=0):
    print(f'Nombre: {nombre}, Apellido: {apellido}, Edad: {edad}')

# Primero llamamos la función pasando los argumentos de forma posicional
imprimir_nombre('Carlos', 'Ibar', 28)
# Llamar la función usando argumentos por nombre
imprimir_nombre(nombre='Carlos', apellido='Ibar', edad=28)
# Llamar la función usando argumentos por nombre, pero intercambiando el nombre
imprimir_nombre(edad=28, apellido='Ibar', nombre='Carlos')
# Argumentos con valor por default
imprimir_nombre(nombre='Carlos')
imprimir_nombre(nombre='Carlos', apellido='Ibar')
imprimir_nombre(apellido='Ibar', nombre='Carlos')