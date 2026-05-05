print(f'*** CREACION Y VALIDACION DE PASSWORD ***')

# Inicializamos variables
pass_valido = False
MINIMO_PASS = 6
pass_creado = input(f'Crea una contraseña: ')

while len(pass_creado) < MINIMO_PASS:
    print(f'El password debe de tener minimo 6 caracteres.')
    pass_creado = input(f'Crea una contraseña: ')

else:
    while not pass_valido:

        pass_solicitado = input(f'Ingresa la contraseña correcta: ')

        if pass_solicitado == pass_creado:
            pass_valido = True

        else:
            print(f'Password incorrecto. Prueba de nuevo.')
    else:
        print('Password Correcto!')
