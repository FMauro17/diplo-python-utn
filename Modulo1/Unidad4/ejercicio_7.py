"""
Ejercicio 7 - Dificultad muy alta
A partir de una funcion recursiva que recorre los niveles de una lista anidada,
optimizarla para que: tome un valor de lista por defecto, reciba un segundo
parametro que registre el nivel de anidamiento (con valor por defecto 0), y
presente la salida indentada segun el nivel.
"""

# Define la lista anidada que se va a recorrer
lista = [
    "elemento1n1", "elemento2n1", "elemento3n1",
    ["elemento1n2", "elemento2n2", "elemento3n2",
     ["elemento1n3", "elemento2n3", "elemento3n3"]],
]

# Recorre una lista anidada e imprime cada elemento con sangria segun su nivel
def recorrer_lista(item=lista, nivel=0):
    # Recorre cada elemento del nivel actual
    for x in item:
        # Si el elemento es una lista, se llama a si misma bajando un nivel
        if isinstance(x, list):
            recorrer_lista(x, nivel + 1)
        # Si no es una lista, lo imprime con la sangria correspondiente al nivel
        else:
            print("    "* nivel + x)

# Llama a la funcion usando los valores por defecto
recorrer_lista()