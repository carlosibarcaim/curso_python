print(f'*** Numero par o impar ***')

apagado = False
# Crear función para saber si el numero es par o impar
def numero_par(numero):
    global apagado
    if numero == 0:
        apagado = True
    elif numero % 2 == 0:
        print(f'El numero {numero} es par')
    elif numero % 2 > 0:
        print(f'El numero {numero} es impar')

# Llamar a la función
while not apagado:
    numero = int(input('Proporciona un numero: '))
    numero_par(numero)
    if apagado:
        break