print(f'*** SISTEMA BANCARIO ***')

salir_sistema_txt = input(f'Desea salir del sistema? (Si/No) ').strip().lower()

if not salir_sistema_txt == 'si':
    print(f'Continuamos en el sistema...')
else :
    print(f'Saliendo del sisistema...')