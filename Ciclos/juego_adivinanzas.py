from random import randint

print(f'*** JUEGO ADIVINANZAS ***')

numero_secreto = randint(1,50)
numero_jugador = 0
intentos = 0
INTENTOS_MAXIMOS = 10

while numero_jugador != numero_secreto:
    numero_jugador = int(input(f'Adivina el número entre 1 y 50: '))
    intentos += 1

    if intentos >= INTENTOS_MAXIMOS:
        print(f'Se te acabó el número de intentos, Has perdido! :( ')
        print(f'El numero secreto era: {numero_secreto}')
        break
    elif numero_jugador > numero_secreto:
        print(f'Intento fallido, te quedan {INTENTOS_MAXIMOS - intentos} intentos')
        print(f'El numero secreto es menor')

    elif numero_jugador < numero_secreto:
        print(f'Intento fallido, te quedan {INTENTOS_MAXIMOS - intentos} intentos')
        print(f'El numero secreto es mayor')

else:
    print(f'Felicitaciones! Adivinaste el número!')