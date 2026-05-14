print(f'*** Lista de Tuplas ***')

productos = [
    ('P001', 'Chamarra', 700.00),
    ('P002', 'Pantalón', 500.00),
    ('P003', 'Camiseta', 250.00)
]

# Imprimir información de cada producto y ademas calcular precio total
precio_total = 0

for producto in productos:
    id, descripcion, precio = producto # Unpacking
    print(f'ID del producto: {id}, Descripcion del producto: {descripcion}, Precio del producto: ${precio:.2f}')
    precio_total += precio

print(f'Precio total: ${precio_total:.2f}')