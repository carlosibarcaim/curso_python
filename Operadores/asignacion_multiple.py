# Asignación multiple

# Asignación multiple
x, y, z = 5, 'Hola', -9.15
print(f'Valor de x = {x}, valor de y = {y}, valor de z = {z}')

# Asignación encadenada
a = b = c = 10
print(f'Valor de a = {a}, valor de b = {b}, valor de c = {c}')

# Intercambio de valores de una variable, sin utilizar variables temporales
x, y = 5, 10
print(f'Valores iniciales x = {x}, y = {y}')
#Aplicando el concepto de asignación multiple, intercambiamos valores
x,y = y,x
print(f'Valores intercambiados x = {x}, valor de y = {y}')

#Entrada de datos con asignación multiple
nombre, apellido = input(f'Ingresa tu nombre y apellido separados por una coma: ').split(',')
print(f'Nombre: {nombre.strip()}')
print(f'Apellido: {apellido.strip()}')



