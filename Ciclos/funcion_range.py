print(f'*** FUNCION RANGE ***')

print(f'Secuencia del 0 al 4')
#Inicio = 0 (opcional)
#Fin = 5 - 1 = 4
#Incremento = 1 (opcional)
for i in range(5): # fin = 5-1
    print(i, end=' ')


print(f'\n\nSecuencia del 10 al 20: ')
# incremento = 1 (default y es opcional)
for i in range(10,20+1):
    print(i, end=' ')

print(f'\n\nSecuencia del 20 al 30 de 2 en 2: ')
for i in range(20,30+1,2):
    print(i, end=' ')