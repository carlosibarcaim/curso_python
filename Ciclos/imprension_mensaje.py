print(f'*** Repetición de un Mensaje ***')

mensaje = input('Proporciona un mensaje a repetir: ')
numero_de_repeticiones = int(input(f'Proporciona el numero de repeticiones: '))

for _ in range(numero_de_repeticiones): #Se usa _ cuando la variable no se utilizará en el for
    print(f'{mensaje}')