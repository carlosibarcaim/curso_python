print(f'*** SISTEMA DE ENVÍOS ***')

# Solicitar al usuario los valores del envío
es_internacional = input(f'El envío es internacional? (Si/No) ').strip().lower()
peso_envio = float(input('Ingresa el peso del paquete (en kg): '))

# Definir Constantes
costo_por_kg = 20 if es_internacional == 'si' else 10

# Determinar el costo del envío
costo_total_envio = peso_envio * costo_por_kg

# Imprimir resultados
print(f'''
El envío es internacional: {es_internacional}
El peso del paquete es: {peso_envio} kg.
Costo por kg: ${costo_por_kg:.2f}

El costo total del envío es: ${costo_total_envio:.2f}
''')