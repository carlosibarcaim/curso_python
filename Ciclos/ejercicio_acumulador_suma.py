print(f'*** Suma acumulativa')

NUMERO_MAXIMO = 5
numero = 1
acumulador_suma = 0

while numero <= NUMERO_MAXIMO:
    acumulador_suma = numero + acumulador_suma
    print(acumulador_suma, end=' ')
    numero += 1