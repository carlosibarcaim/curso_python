print(f'*** VALOR DENTRO RANGO ***')

# Valores de rango
VALOR_MINIMO = 0
VALOR_MAXIMO = 5

# Pedir al usuario que ingrese un numero
valor_usuario = int(input(f'Introduce un valor numerico entre {VALOR_MINIMO} y {VALOR_MAXIMO}: '))

# Validar si el valor está dentro del rango
valor_dentro_rango = VALOR_MINIMO <= valor_usuario <= VALOR_MAXIMO

#Imprimir si el valor está dentro del rango
print(f'El valor del usuario está dentro del rango: {valor_dentro_rango}')