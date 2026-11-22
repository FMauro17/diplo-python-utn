"""
Ejercicio 5 - Dificultad media
Cree un programa que utilizando una funcion, solicite la edad de la persona e
imprima todos los años que la persona ha cumplido, en orden ascendente y
descendente, separados por comas.
"""

# Recibe una edad e imprime los años cumplidos en orden ascendente y descendente
def mostrar_anios(edad):
    # Imprime del 1 hasta la edad, separados por coma
    print(*range(1, edad, + 1), sep= ", ")
    print("Y")
    # Imprime de la edad hasta el 1, separados por coma
    print(*range(edad, 0, - 1), sep= ", ")

# Pide la edad al usuario y la convierte a entero
edad = int(input("Ingrese la edad: "))

# Llama a la funcion con la edad ingresada
mostrar_anios(edad)