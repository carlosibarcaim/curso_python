print(f'*** Imprimir detalles de una persona usando kwargs ***')

numero_persona = 0
# Funcion que acepta argumentos vaiables en forma de kwargs
def imprimir_detalle_persona(**kwargs):
    global numero_persona
    numero_persona += 1
    print(f'\nValores recibidos persona {numero_persona}: ')
    for llave, valor in kwargs.items():
        print(f'{llave}: {valor}')

imprimir_detalle_persona(nombre='Carlos', apellido='Ibar', edad=28, puesto='Programador')
imprimir_detalle_persona(nombre='Jorge' ,apellido='Ibar' , edad=17 , escuela='Cetis 36' )
imprimir_detalle_persona(nombre='Fernanda' ,apellido='Cadena' , edad=17 , escuela='Cetis 36' )
imprimir_detalle_persona(nombre='Jessica' ,apellido='Ibar' , edad=17 , puesto='Psicologa' )