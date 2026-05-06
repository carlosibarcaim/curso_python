# Ejemplo: Cadenas inmutables

animal = "Gato"

#animal[4] = "s" # Provoca un error
#CORRECTO: Concatenar (Sumar)
#Tomamos "gato" + s y lo guardamos en una nueva variable
plural = animal + "s"
print(animal)
print(plural)

plural = f"{animal}s"
print(plural) 