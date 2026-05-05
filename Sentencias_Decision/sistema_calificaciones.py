print(f'*** SISTEMA DE CALIFICACIONES ***')

# Pedir al usuario la calificacion en número
calificacion_numerica = float(input('Escribe una calificación del 1 al 10: '))

# Definir calificación con literal
if calificacion_numerica >= 9 and calificacion_numerica <= 10:
    calificacion_literal = 'A'
elif calificacion_numerica >= 8 and calificacion_numerica < 9:
    calificacion_literal = 'B'
elif calificacion_numerica >= 7 and calificacion_numerica < 8:
    calificacion_literal = 'C'
elif calificacion_numerica >= 6 and calificacion_numerica < 7:
    calificacion_literal = 'D'
elif calificacion_numerica >= 0 and calificacion_numerica < 6:
    calificacion_literal = 'F'
else:
    calificacion_literal = 'Valor Desconocido'

# Imprimir resultado
print(f'''
Calificación numérica: {calificacion_numerica}
Calificacion con letra: {calificacion_literal}
''')