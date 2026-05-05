print(f'*** CASA DE LOS ESPEJOS ***')

# Datos del usuario
EDAD_MINIMA = 10
edad = int(input(f'Que edad tienes? '))
miedo_oscuridad = input('Te da miedo la oscuridad? (Si/No) ').strip().lower()

# Condiciones
if edad >= EDAD_MINIMA and not miedo_oscuridad == 'si':
    print(f'Felicidades! Puedes entrar a la casa de los espejos')
else:
    print(f'No puedes entrar a la casa de los espejos')