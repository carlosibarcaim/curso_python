# Crear programa generador de emails

print('*** Sistema Generador de Email ***\n')

# Pedir al usuario que ingrese los datos
nombre = input('Ingresar nombres: ')
apellidos = input('Ingresar apellidos: ')
empresa = input('Ingresar nombre de la empresa: ')

# Tratamiento de datos
nombre_usuario = nombre.strip().lower().replace(' ', '.')
apellidos_usuario = apellidos.strip().lower().replace(' ', '.')
empresa_usuario = empresa.strip().lower().replace(' ','')
dominio = '.com.mx'

#Generar email del usuario
email = nombre_usuario + '.' + apellidos_usuario + '@' + empresa_usuario + dominio

#Imprimir mensaje al usuario con email generado
print(f'''
    Hola {nombre},
        Tu email generado es: {email}
''')
