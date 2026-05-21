print(f'*** Alcance variables ***')

contador_global = 0

def incremetar_contador():
    contador_local = 0
    global contador_global
    #Incrementar los contadores local y global
    contador_local += 1
    contador_global += 1
    # Imprimir los contadores
    print(f'Contador local: {contador_local}')
    print(f'Contador global: {contador_global}\n')

# Llamar varias veces a la función
incremetar_contador()
incremetar_contador()
incremetar_contador()