print(f'*** CONTADOR DE VOCALES ***')

# Declarar variable
cadena = 'Hola Mundo'
vocales = ['a','e','i','o','u']
numero_letras = 0

# Agregar el ciclo for
for vocal in vocales:
    for letra in cadena:
        if letra == vocal:
            numero_letras += len(letra)

# Imprimir la cantidad de vocales encontradas en la cadena
print(numero_letras)