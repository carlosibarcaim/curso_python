print(f'*** CALCULO DE AREA Y PERIMETRO DE UN RECTANGULO ***')

# Pedir valores al usuario
base = float(input(f'Ingresa el valor de la base: '))
altura = float(input(f'Ingresa el valor de la altura: '))

# Calculos
perimetro = 2 * (base + altura)
area = base * altura

# Imprimir resultados
print(f'''
El valor de la base es: {base}
El valor de la altura es: {altura}
El valor del perimetro es: {perimetro}
El valor del area es: {area}
''')