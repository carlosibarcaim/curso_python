print(f'*** Sistmea Descuentos VIP ***')

# Asignar valores
PRODUCTOS_MINIMOS = 10
cantidad_productos = int(input(f'Cuantos productos compró? '))
es_cliente_vip = input(f'Cuenta con membresía? (Si/NO)').lower().strip()

tiene_descuento = cantidad_productos >= PRODUCTOS_MINIMOS and es_cliente_vip == 'si'

print(f'El cliente tiene descuento VIP: {tiene_descuento}')