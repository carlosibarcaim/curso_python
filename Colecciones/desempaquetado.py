print(f'*** Desempaquetado de Tuplas ***') # Unpacking

producto = ('P001', 'Camisa', 20.00)

# Desempaquetado
id, descripcion, precio = producto

# Mostrar valores, ya desempaquetados
print(f'Tupla completa: {producto}')
print()
print(f'Id del producto: {id}\nDescripción del producto: {descripcion}\nPrecio del producto: {precio}')