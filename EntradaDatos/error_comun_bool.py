# ERROR COMUN DE PRINCIPIANTE
from gettext import textdomain

respuesta_usuario = "False"

es_verdad = bool(respuesta_usuario)
print(f'El valor del texto "False" es: {es_verdad}')

texto_vacio = ""
es_falso = bool(texto_vacio)
print(f'El valor del texto vacío es: {es_falso}')