print(f'*** SISTEMA DE AUTENTICACIÓN ***')

# Valores correctos del usuario
USUARIO = 'carlos.ibar@itw.mx'
PASSWORD = 'Itw#2604'

# Pedir al usuario que introduzca usuario y contraseña
usuario_introducido = input(f'Introduzca el usuario: ').lower().strip()
password_introducido = input(f'Introduzca contraseña: ')

# Validar usuario y contraseña
usuario_correcto = USUARIO == usuario_introducido
password_correcto = PASSWORD == password_introducido
credenciales_correctas = usuario_correcto and password_correcto

# Imprimir True o False si el usuario y contraseña son correctos o no
print(f'El usuario se ha logeado de forma exitosa: {credenciales_correctas}')