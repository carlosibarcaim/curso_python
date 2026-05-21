print(f'*** Regresar una tupla de valores desde una función ***')

# Definición de la función
def persona_mayusculas(nombre, apellido, edad):
    print(f'Esta función regresa varios valores (tupla)')
    return nombre.upper(), apellido.upper(), edad

# Programa principal
nombre, apellido, edad = persona_mayusculas('Carlos', 'ibar', 28)
print(f'Resultado persona: nombre: {nombre}, apellido: {apellido}, edad: {edad}')