"""
Ejercicio 1 - Dificultad baja
Cree una función lambda que compruebe si un número es par o impar.
"""

# Define una funcion lambda que recibe un numero y devuelve es par o impar
es_par = lambda numero: "Par" if numero % 2 == 0 else "Impar"

# Llama lambda con distintos numeros y muestra el resultado
print(es_par(4))
print(es_par(7))
print(es_par(5))
print(es_par(10))