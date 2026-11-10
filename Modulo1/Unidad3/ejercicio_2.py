"""
Ejercicio 2 (M1-U3)
Escriba un programa que consulte al usuario por una oración y comente
al usuario cuántas veces aparece la letra "a".
"""

# Pide una oracion al usuario
oracion = input("Ingrese una oracion: ")

# Inicializa el contador de apariciones de la letra "a"
contador = 0

# Recorre cada caracter de la oracion
for caracter in oracion:
    # Suma uno al contador cuando el caracter es la letra "a"
    if caracter == "a":
        contador += 1

# Muestra cuantas veces aparecio la letra "a"
print(f"La letra 'a' aparece {contador} veces")