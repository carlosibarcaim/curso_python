print(f'*** TIENDA EN LINEA ***')

#Pedir al usuario su monto de la compra y preguntar si es miembro
MONTRO_COMPRA_DESC = 1000

monto_compra = float(input(f'Ingrese el monto de su compra: '))
es_miembro = input(f'Es miembro de la tienda? Si/No ').strip().lower()

if monto_compra >= MONTRO_COMPRA_DESC and es_miembro == 'si':
    #Definir valores y descuento
    descuento = monto_compra * .10
    monto_compra_final = monto_compra - descuento

elif monto_compra <= MONTRO_COMPRA_DESC and es_miembro == 'si':
    #Definir valores y descuento
    descuento = monto_compra * .05
    monto_compra_final = monto_compra - descuento

else:
    #Definir valores y descuento
    descuento = 0
    monto_compra_final = monto_compra

print(f'''
Monto de la compra: {monto_compra:.2f}
Descuento: {descuento:.2f}
Monto Total a Pagar: {monto_compra_final:.2f}
''')