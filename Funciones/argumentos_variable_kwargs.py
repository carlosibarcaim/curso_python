print(f'*** Argumentos kwarg ***')

def superheroe_superpoderes(nombre, *args, **kwargs):
    print(f'superheroe: {nombre}')
    for superpoder in args:
        print(f'\tSuperpoder: {superpoder}')

    print(f'Mas info del superheroe: ')
    for llave, valor in kwargs.items():
        print(f'\t{llave}: {valor}')

    print()

superheroe_superpoderes('Spiderman', 'Telaraña', 'Sentido aracnido', edad=17, empresa='marvel')
superheroe_superpoderes('Ironman', 'Armadura', edad=45, empresa='marvel', ocupacion='Playboy')