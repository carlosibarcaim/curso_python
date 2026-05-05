print(f'*** IDENTIFICA LA ESTACIÓN DEL AÑO ***')

# Pedir al usuario el mes
mes_usuario = int(input(f'Selecciona un mes del 1 al 12 para saber la estación del año: '))

# Definir que estación del año es mediante las condiciones
if mes_usuario in (1,2,12):
    estacion = 'Invierno'
elif mes_usuario in (3,4,5):
    estacion = 'Primavera'
elif mes_usuario in (6,7,8):
    estacion = 'Verano'
elif mes_usuario in (9,10,11):
    estacion = 'Otoño'
else:
    estacion = 'Estación Desconocida'

# Imprimir el resultado
print(f'''
Seleccionaste el mes: {mes_usuario}
La estación del mes seleccionado es: {estacion}
''')