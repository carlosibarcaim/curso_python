from dis import print_instructions
from tokenize import endpats

print(f'*** Diccionarios en Python ***')

# Crear dict de persona con clave valor
persona = {
    'nombre': 'Carlos',
    'apellido': 'Ibar',
    'edad': 28,
    'ciudad': 'Edo Mex'
}

print(f'Diccionario de persona: {persona}')

# Acceder a los elementos de la página
print(f'Nombre: {persona['nombre']}')
print(f'Apellido: {persona.get('apellido')}')
print(f'Edad: {persona['edad']}')
print(f'ciudad: {persona.get('ciudad')}')

# Modificar un valor del diccionario
persona['edad'] = 30
print(f'Diccionario de persona: {persona}')

# Agregar un nuevo elemento
persona['profesion'] = 'Programador'
print(f'Diccionario de persona: {persona}')

# Eliminar un elemento
del persona['ciudad']
print(f'Diccionario de persona: {persona}')

persona.pop('profesion')
print(f'Diccionario de persona: {persona}')

# Iterar elementos de un dict (llave, valor)
for llave, valor in persona.items():
    print(f'Llave: {llave}, Valor: {valor}')

# Iterar solamente valores de un dict
for valor in persona.values():
    print(f'-Valor: {valor}')

# Iterar solamente llaves de un dict
for llave in persona.keys():
    print(f'-Llave: {llave}')