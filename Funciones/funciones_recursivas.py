print(f'*** Funciones recursivas ***')

# Crear funcion para cuenta regresiva
def cuenta_regresiva(numero):
    if numero == 0: # Caso base
        print(numero, end=' ')
        return numero
    elif numero > 0:
        print(numero, end=' ')
        cuenta_regresiva(numero - 1) # Llamada Recursiva

# Pedir al usuario el numero
numero = int(input(f'Escribe un numero para realizar la cuenta regresiva: '))
cuenta_regresiva(numero)