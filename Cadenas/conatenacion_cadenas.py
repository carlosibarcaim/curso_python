# Programa: Ejemplo de concatenacion de cadenas

# 1. Usando el operador +
nombre = 'Carlos'
apellido = 'Ibar'
nombre_completo = nombre + " " + apellido
print("Usando + : " + nombre_completo)

# 2. Usando el metodo print
edad = 28
print("Usando comas:", "Nombre:", nombre_completo, "Edad:", edad)

# Usando f-string
ciudad = 'EdoMex'
pais = 'México'
profesion = 'Desarrollador Jr'
presentacion = f"Hola, soy {nombre_completo}, tengo {edad} años y soy {profesion} en {ciudad}, {pais}"
print(presentacion)