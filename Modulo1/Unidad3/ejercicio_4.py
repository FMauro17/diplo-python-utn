"""
Ejercicio 4 (M1-U3)
Escriba un programa que solicite la edad de la persona e imprima
todos los años que la persona ha cumplido.
"""

# Pide la edad a la persona y la convierte a entero
edad = int(input("Ingrese su edad: "))

# Recorre desde el año 1 hasta la edad ingresada, incluyendola
for anio in range(1, edad +1):
    # Muestra el año cumplido actual
    print(f"Cumplio {anio} años.")