# Sistema para generar ID unico para usuarios
from idlelib.search import find
from random import randint

print('*** Generador de ID unico\n')

# Pedir los datos al usuario
nombre = input('Ingresar Nombre: ')
apellido = input('Ingresar Apellido: ')
anio_nacimiento = input('Ingresar año de nacimiento (YYYY): ')

# Generar valor aleatorio
numero_aleatorio = randint(1000,9999)

# Tratar datos
nombre_usuario = nombre.strip().upper()[0:2]
apellido_usuario = apellido.strip().upper()[0:2]
anio_nacimiento_usuario = anio_nacimiento.strip()[2:4]
numero_aleatorio_usuario = str(numero_aleatorio)

# Generar ID de usuario
id_usuario = nombre_usuario + apellido_usuario + anio_nacimiento_usuario + numero_aleatorio_usuario

# Imprimir mensaje con ID generado del usuario
print(f'''
    Hola {nombre_usuario}.
        Se ha generado tu ID de usuario: {id_usuario}.
        Felicidades!
''')