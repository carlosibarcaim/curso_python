print(f'*** SISTEMA RESERVA HOTEL ***')

# Solicitar datos al usuario
nombre_cliente = input('Ingrese el nombre del cliente: ').strip()
dias_estadia = int(input('Cuantos días de estadía tendrá? '))
tiene_vista_mar = input(f'Tiene vista al mar? (Si/No) ').strip().lower()

# Tarifas, definir constantes
PRECIO_CUARTO = 190.50 if tiene_vista_mar == 'si' else 150.50

# Calculo de costo total de la estadía
costo_total = PRECIO_CUARTO * dias_estadia

# Imprimir cotización de hotel
print(f'''
Cliente: {nombre_cliente}
Días: {dias_estadia}
Tiene vista al mar? {tiene_vista_mar}

Costo por día: ${PRECIO_CUARTO:.2f}
Costo total de la estadía en la habtación: ${costo_total:.2f}
''')
