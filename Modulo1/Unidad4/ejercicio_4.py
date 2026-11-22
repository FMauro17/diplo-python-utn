"""
Ejercicio 4 - Dificultad alta
Crear una funcion lambda que tome como parametro una frase y la escriba al reves.
"""

# Define una lambda que recibe una frase y la devuelve invertida
invertir = lambda frase: frase[::-1]

# Llama a lambda con una frase y muestra el resultado
print(invertir("hola mundo"))