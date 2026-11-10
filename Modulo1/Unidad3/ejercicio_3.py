"""
Ejercicio 3 (M1-U3)
Escriba un programa que consulte al usuario por una oración y comente
al usuario cuántas veces aparecen todas las vocales considerando minúsculas,
mayúsculas y acentos.
"""

# Pide una oracion al usuario
oracion = input("Ingrese una oracion: ")

# Convierte toda la oracion a minuscula para unificar mayusculas y minusculas
texto = oracion.lower()

# Define el reemplazo de cada vocal acentuada por su version simple
acentos = {"á": "a", "é": "e", "í": "i", "ó": "o", "ú": "u","ü": "u"}

# Reemplaza en el texto cada vocal acentuada por su version sin acento
for acentuada, simple in acentos.items():
    texto = texto.replace(acentuada, simple)

# Inicializa el diccionario que acumula el conteo de cada vocal
vocales = {"a": 0, "e": 0, "i": 0, "o": 0, "u": 0}

# Recorre cada caracter del texto ya normalizado
for caracter in texto:
    # Suma uno en la vocal correspondiente cuando el caracter es una vocal
    if caracter in vocales:
        vocales[caracter] += 1

# Recorre el diccionario y muestra el conteo de cada vocal
for vocal, cantidad in vocales.items():
    print(f"La vocal '{vocal}' aparece {cantidad} veces.") 