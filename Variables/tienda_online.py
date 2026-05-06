#Crear Sistema de Tienda Online
# Crear el detalle de un producto de una tienda online, el detalle debe tener:
# 1.-Nombre del producto, 2.-Precio del producto, 3.-Cantidad en el inventario, 4.-Indicar si está disponible
# Hacer algunos cambios y mandar a imprimir nuevamente el nuevo valor de las variables

print('*** Sistema de Tienda Online ***')

# Definir valores de las Variables
nombre_producto = 'Audifonos Logitech'
precio_producto = 2400.0
cantidad_en_inventario = 20
disponible_para_entrega = True

# Imprimir valores
print('Nombre del producto: ',nombre_producto)
print('Precio del producto: $',precio_producto)
print('Cantidad de productos en inventario: ',cantidad_en_inventario)
print('El producto está disponible? ',disponible_para_entrega)

# Modificar valores de las variables
nombre_producto = 'Mouse Razer'
precio_producto = 800.99
cantidad_en_inventario = 0
disponible_para_entrega = False

# Imprimir valores modificados
print()
print('Nombre del producto: ',nombre_producto)
print('Precio del producto: $',precio_producto)
print('Cantidad de productos en inventario: ',cantidad_en_inventario)
print('El producto está disponible? ',disponible_para_entrega)