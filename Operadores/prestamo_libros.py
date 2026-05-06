print(f'*** Sistema Prestamo de Libros ***')

# Asignación de valores
KM_REDONDA_MAXIMO = 3
km_distancia_usuario = int(input(f'¿A cuantos km de distancia vive? '))
tiene_credencial = input(f'¿Cuenta con credencial de estudiante? (Si/No)').lower().strip()

tiene_prestamo_libro = km_distancia_usuario <= KM_REDONDA_MAXIMO or tiene_credencial == 'si'

print(f'El usuario es candidato a prestamo de libro: {tiene_prestamo_libro}')