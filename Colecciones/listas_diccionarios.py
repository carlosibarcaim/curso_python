print(f'*** LISTA DE DICCIONARIOS ***')

personas = [
    {
        'nombre': 'Regina',
        'apellido': 'Flores',
        'edad': 21,
    },
    {
        'nombre': 'Alejandro',
        'apellido': 'Reyes',
        'edad': 32,
    }
]

print(personas)

# Acceder a un diccionario desde una lista
print(f'''
    Nombre: {personas[0].get('nombre')}
    Apellido: {personas[0].get('apellido')}
    Edad: {personas[0].get('edad')}
''')

# Recorrer los elementos de la lista
print()
for contador, persona in enumerate(personas):
    print(f'{contador + 1} - {persona}')
    print(f'Detalle: Nombre: {persona.get('nombre')}, Apellido: {persona.get('apellido')}, Edad: {persona.get('edad')}')