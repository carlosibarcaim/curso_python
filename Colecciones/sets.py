print(f'*** Sets ***')

mi_set = {1,2,3,4,5,4}
print(f'mi_set: {mi_set}')

# Agregar elementos al set
mi_set.add(7)
mi_set.add(6)
print(f'Añadi elementos a mi_set: {mi_set}')

# Intentar agregar un elemento duplicado al set
mi_set.add(5)
print(f'Agregar elemento duplicado: {mi_set}')

# Eliminar un elemento del set
mi_set.remove(4)
print(f'Elemento eliminado del set: {mi_set}')

# Iterar los elementos del set
for elemento in mi_set:
    print(elemento,end=' ')

# Comprobar si existe un elemento en el set
print(f'\nExiste el valor 1 en el set? {1 in mi_set}')

# Obtener la longitud del set
print(f'Longitud del set: {len(mi_set)}')