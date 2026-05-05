print(f'*** MAYOR DE 2 NUMEROS ***')

# Datos pedidos al usuario
numero1 = int(input(f'Ingresar el primer número: '))
numero2 = int(input(f'Ingresar el segundo número: '))

# Comparar los números y elegir al mayor
if numero1 > numero2:
    numero_mayor = numero1
elif numero1 < numero2:
    numero_mayor = numero2
else:
    numero_mayor = 'son iguales'

# Imprimir el resultado
print(f'''
El primer numero es: {numero1}
El segundo numero es: {numero2}

El numero mayor es: {numero_mayor}
''')