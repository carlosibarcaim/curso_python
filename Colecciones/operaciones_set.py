print(f'*** Operaciones con Set ***')

a = {1,2,3,4}
b = {3,4,5,6}

# Union de sets
union = a | b
print(f'Union de a y b: {union}')

# Interseccion de sets
interseccion = a & b
print(f'Interseccion de a y b: {interseccion}')

# Diferencia de sets
diferencia = a - b
print(f'Diferencia de a y b: {diferencia}') # En vez de diferencia se restan los valores existentes de un set a otro