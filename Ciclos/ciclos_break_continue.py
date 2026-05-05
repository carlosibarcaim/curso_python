print(f'*** CICLOS BREAK Y CONTINUE ***')

# Ejemplo break
print(f'Ejercicio con break: ')
for numero in range(1,10):
    if numero % 2 == 0: # numero par
        print(numero)
        break

# Ejemplo continue
print(f'\nEjercicio con continue: ')
for numero in range(1,10):
    if numero % 2 > 0: # numero impar
        continue
    print(numero)