print(f'*** Generación de Ticket de Compra ***')

#Productos
precio_huevo = float(input(f'Introducir el precio del huevo: '))
precio_leche = float(input(f'Introducir el precio de la leche: '))
precio_pan = float(input(f'Introducir el precio del pan: '))
precio_lechuga = float(input(f'Introducir el precio de la lechuga: '))
descuento = float(input(f'Introduzca el porcentaje del descuento: ')) / 100

# Calculo de valores
subtotal_compra = (precio_huevo + precio_leche + precio_pan + precio_lechuga)
descuento_aplicado = subtotal_compra * descuento
subtotal_descuento_aplicado = subtotal_compra - descuento_aplicado
IMPUESTO_COMPRA = .16
impuesto_compra = subtotal_descuento_aplicado * IMPUESTO_COMPRA
total_compra = subtotal_descuento_aplicado + impuesto_compra

#Mandar a imprimir datos del ticket
print(f'********** TICKET DE COMPRA **********')
print(f'Huevo: ${precio_huevo:.2f}')
print(f'Leche: ${precio_leche:.2f}')
print(f'Pan: ${precio_pan:.2f}')
print(f'Lechuga: ${precio_lechuga:.2f}')
print(f'\nSubtotal: ${subtotal_compra:.2f}')
print(f'Descuento aplicado: {descuento_aplicado:.2f}')
print(f'Subtotal con descuento aplicado: {subtotal_descuento_aplicado:.2f}')
print(f'Impuestos: ${impuesto_compra:.2f}')
print(f'TOTAL: ${total_compra:.2f}')
