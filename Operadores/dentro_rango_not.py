print(f'*** Valor dentro de rango')

valor = int(input('Proporcione un numero: '))
valor_dentro_rango = 1 <= valor <= 10

esta_fuera_rango = not(valor_dentro_rango)

print(f'El numero {valor} está fuera del rango: {esta_fuera_rango}')