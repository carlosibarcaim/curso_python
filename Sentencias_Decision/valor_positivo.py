print(f'*** VALOR POSITIVO ***')

# Pedir al usuario un número
numero = int(input('Ingresa un numero para saber si es positivo o negativo: '))

# Definir si es positivo negativo o cero
if numero > 0:
    print(f'El número que ingresaste: {numero}, es positivo')
elif numero < 0:
    print(f'El numero que ingresaste: {numero}, es negativo')
else:
    print(f'El número que ingresaste: {numero}, es cero') 