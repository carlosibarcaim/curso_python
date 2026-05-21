print(f'*** Argumentos Variables ***')

def superheroe_superpoderes(superheroe, nombre, *args):
    print(f'Superheroe: {superheroe} - {nombre}')
    # Iteramos los superpoderes
    for superpoder in args:
        print(f'\tsuperpoder: {superpoder}')
    print()

# Llamar a la función
superheroe_superpoderes('Spiderman', 'Peter Parker', 'Trepar', 'Lanzar telarañas', 'Sentido aracnido')
superheroe_superpoderes('Ironman', 'Tony Stark', 'Armadura')
superheroe_superpoderes('Carlos Ibar', 'Carlos Ibar')