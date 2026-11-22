"""
Ejercicio 6 - Dificultad alta
Cree una funcion que tome una lista y reordene de menor a mayor sus componentes.
[3, 44, 21, 78, 5, 56, 9]
"""

# Recibe una lista y la ordena de menor a mayor en el lugar
def ordenar_lista(lista):
    lista.sort()

# Crea la lista con los numeros a ordenar
numeros = [3, 44, 21, 78, 5, 56, 9]

# Ordena la lista llamando a la funcion
ordenar_lista(numeros)

# Miestra la lista ya ordenada
print(numeros)
