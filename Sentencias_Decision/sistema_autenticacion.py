print(f'*** SISTEMA DE AUTENTICACIÓN ***')

# Definir constantes USUARIO y PASSWORD
USUARIO = 'carlos.ibar@itw.mx'
PASSWORD = 'Itw#2604'

# Solicitar datos al usuarios
usuario = input(f'Ingresa el usuario: ').strip().lower()
password = input(f'Ingresa la contraseña: ')

if usuario == USUARIO and password == PASSWORD:
    print(f'Usuario logeado con exito!')
elif usuario == USUARIO and password != PASSWORD:
    print(f'Contraseña invalida.')
elif usuario != USUARIO and password == PASSWORD:
    print(f'Usuario invalido.')
else:
    print(f'Usuario y contraseña invalidos')