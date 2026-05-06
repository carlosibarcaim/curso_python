# Crear un programa para generar un email apartir de los siguientes datos:
#-Nombre: carlos alberto ibar mendoza
#-Empresa: itw
#-Dominio: .com.mx
#Resultado final: carlos.alberto.ibar.mendoza@itw.com.mx

print("*** Generador de Email ***")

# Normalizar nombre de usuario
nombre_usuario = 'Carlos Alberto Ibar Mendoza'
nombre_usuario_normalizado = nombre_usuario.lower().replace(" ", ".")

# Normalizar el dominio
nombre_empresa = 'ITW'
extension_dominio = '.com.mx'
dominio_email_normalizado = f"@{nombre_empresa.lower()}{extension_dominio}"

# Mostrar el email generado
email_generado = f"{nombre_usuario_normalizado}{dominio_email_normalizado}"
print(email_generado)

texto = "Aprender Python es divertido"
print(texto.find("Python"))