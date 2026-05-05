print(f'*** Lista de repoducción ***')

# Pedir al usuario el numero de las canciones y las canciones
lista_canciones = []
numero_canciones = int(input(f'Ingrese el numero de canciones que desea agregar a la lista: '))

for indice in range(numero_canciones):
    cancion = input(f'Ingrese la canción {indice + 1}: ')
    lista_canciones.append(cancion)

lista_canciones.sort()
print(f'Tu lista de reproducción: \n')
for cancion in lista_canciones:
    print(cancion)


# De esta forma lo hice yo y también funciona

#while len(lista_canciones) < numero_canciones:
#    cancion = input(f'Ingresa el nombre de la canción: ')
#    lista_canciones.append(cancion)

#print(f'Tu lista de canciones es: ')
#lista_canciones.sort()
#for cancion in lista_canciones:
#    print(cancion)

