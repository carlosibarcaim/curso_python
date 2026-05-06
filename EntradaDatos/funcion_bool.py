# Programa: funcion bool

# 1.Numeros (Int y Float)

print(bool(0))      # False (El vacío numérico)
print(bool(0.0))    # False
print(bool(42))     # True (Existe valor)

# 2. Cadenas de texto
# Cadena vacía = False
print(bool(""))     #False

# Cadena con algo = True
print(bool(" "))    #True
print(bool("Hola")) #True

# 3. None (Ausencia total)
print(bool(None))   #False

# Falsos o verdaderos
print(bool(False))  #False
print(bool(True))   #True