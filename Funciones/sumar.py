#import modulo_funcion_sumar
from modulo_funcion_sumar import sumar

print(f'*** Funcion de sumar ***')

# Llamar a la función
if __name__ == '__main__':
    resultado_funcion = sumar(5, 5)
    print(f'Resultado de la función sumar: {resultado_funcion}')

    resultado_funcion = sumar(20, 3)
    print(f'Resultado de la función sumar: {resultado_funcion}')
