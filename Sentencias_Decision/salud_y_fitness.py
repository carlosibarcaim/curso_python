print(f'*** APLICACIÓN DE SALUD Y FITNESS ***')

# Solicitar datos al usuario
nombre_usuario = input(f'Ingresar nombre del usuario: ').strip()
pasos_caminados = int(input(f'Ingresa los pasos caminados en el día: '))

# Definir constantes
META_PASOS_DIARIOS = 10000
CALORIAS_POR_PASO = 0.04 #Valor aproximado en kilocalorias

# Calcular calorias quemadas segun los pasos caminados
calorias_quemadas = pasos_caminados * CALORIAS_POR_PASO

# Verificar si se cumplió la meta de pasos diarios
cumplio_meta = 'Si' if pasos_caminados >= META_PASOS_DIARIOS else 'No'

# Imprimir resultados
print(f'''
Hola, {nombre_usuario}.
El día de hoy caminaste: {pasos_caminados} pasos, por lo cual quemaste {calorias_quemadas} kilocalorías.
Cumpliste tu meta de pasos díarios? {cumplio_meta}
''')