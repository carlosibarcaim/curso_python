print(f'*** PROMEDIO DE CALIFICACIONES ***')

# Pedimos al usuario el numero de materias
numero_materias = int(input(f'Ingresa el número de materias: '))
calificaciones = []

# Iteramos el numero de materias para que el usuario registre cada una
for materia in range(numero_materias):
    calificacion = float(input(f'Ingresa la calificación de la materia {materia + 1}: ' ))
    calificaciones.append(calificacion)

# Calcular el promedio e imprimirlo
promedio = sum(calificaciones) / numero_materias
print(f'Promedio de calificaciones: {promedio:.1f}')