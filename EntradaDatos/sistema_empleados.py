# Programa: Sistema para empleados
print(f'*** SISTEMA DE EMPLEADOS ***')
print(f'Ingresa la información al sistema de empleados.')

# Pedir datos a usuario
nombre_empleado = input(f'Ingresar nombre del empleado: ')
edad_empleado = int(input(f'Ingresar edad del empleado: '))
salario_empleado = float(input(f'Ingresar salario del empleado: '))
es_jefe_departamento = input(f'Es jefe de departamento (Si/No)? ')

#Convertir a tipo bool si es jefe de departamento o no
es_jefe_departamento = es_jefe_departamento.lower() == 'si'

print(f'''
        Información del Empleado:
    Nombre del empleado: {nombre_empleado}
    Edad del empleado: {edad_empleado} años
    Salario del empleado: ${edad_empleado:.2f} 
    Es jefe de departamento: {es_jefe_departamento}
''')