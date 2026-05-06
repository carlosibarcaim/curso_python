# Valores aleatorios con la funcion randint
import random
from random import randint

# Generar un número aleatorio entre 1 y 10
numero = random.randint(1,10)
print(f'El número aleatorio entre 1 y 10 es: {numero}')

# Simular un dado de 6 caras
dado = random.randint(1,6)
print(f'La cara del dado es: {dado}')

# Simular dos dados de 6 caras
dado1 = randint(1,6)
dado2 = randint(1,6)
print(f'El resultado de los dados es: {dado1} y {dado2} \n en total es: {dado1 + dado2}')