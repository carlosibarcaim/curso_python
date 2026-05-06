# Programa: Aplicar el concepto de slicing

texto = "PROGRAMACION"

# 1. Básico [Inicio:Fin]
print(texto[0:4]) # "PROG" (El indice 4 no se incluye)

# 2. Atajo desde el inicio [:Fin]
print(texto[:4]) # "PROG" (Asume inicio 0)

# 3. Atajo hasta el final [Inicio:]
print(texto[8:]) # "CION" (Hasta el último char)

# 4. Indices negativos
print(texto[-4:]) # "CION" (Los últimos 4)

# 5. Pasos [::Paso]
print(texto[::-1]) # NOICAMARGORP (Invertir cadena)
