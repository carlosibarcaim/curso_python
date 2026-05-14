from iterar_listas import nombre

print(f'*** AGENDA DE CONTACTOS ***')

# Crear diccionario de diccionarios
agenda = {
    'Carlos': {
        'telefono': '5633320649',
        'email': 'carlosibarcaim@gmail.com',
        'direccion': 'Villas de San José, Tultitlán'
    },
     'Jorge': {
        'telefono': '5655555555',
        'email': 'jorgeibar@gmail.com',
        'direccion': 'Villas de San José, Tultitlán'
    },
    'Jessica': {
        'telefono': '5510468370',
        'email': 'jessibar@gmail.com',
        'direccion': 'Villas de San José, Tultitlán'
    }
}

print(f'{agenda}')

# Acceder a información de un contacto especifico
print(f'''Información de Carlos: 
Telefono: {agenda['Carlos']['telefono']}
Email: {agenda['Carlos']['email']}
Direccion: {agenda['Carlos']['direccion']}
''')

# Agregar un contacto
agenda['Fernanda'] = {
    'telefono': '5555555555',
    'email': 'fernanda.ibar@gmail.com',
    'direccion': 'monte 123'
}
print(agenda)

# Eliminar un contacto
agenda.pop('Carlos')
print(agenda)

# Mostramos los contactos de la agenda
for contacto, detalles in agenda.items():
    print(f'''
    Nombre: {contacto}
    Telefono: {detalles['telefono']}
    Email: {detalles['email']}
    Direccion: {detalles['direccion']}
''')

# Iterar nombres
for contacto in agenda:
    print(f'-Contacto: {contacto}')

# Iterar telefonos
for contacto, detalles in agenda.items():
    print(f'-Telefono: {detalles['telefono']}')

# Iterar emails
for contacto, detalles in agenda.items():
    print(f'-Email: {detalles['email']}')

# Iterar direcciones
for contacto, detalles in agenda.items():
    print(f'-Direccion: {detalles['direccion']}')