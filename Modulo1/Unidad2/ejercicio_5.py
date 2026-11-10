"""
Ejercicio 5 (M1-U2)
Realice nuevamente los ejercicios 3 y 4, pero utilizando una función,
de forma que la operación se realice dentro de la misma.
Presente el resultado en la terminal del editor.
"""

# DEFINE LA EDAD DE JUBILACION COMO CONSTANTE
EDAD_JUBILACION = 65

# RECIBE 2 VALORES Y DEVUELVE UNA LISTA CON AMBOS Y SU SUMA
def sumar_valores(primer_valor, segundo_valor):
    return [primer_valor, segundo_valor, primer_valor + segundo_valor]

# RECIBE UNA EDAD Y DEVUELVE EL MENSAJE QUE CORRESPONDE
def verificar_jubilacion(edad):
    if edad >= EDAD_JUBILACION:
        return "Ya esta en edad de jubilarse"
    else:
        return "Aun esta en edad de trabajar"

# PIDE LOS DATOS DEL EJERCICIO 3 Y USA LA FUNCION DE SUMA
primer_valor = int(input("Ingrese el primer valor: "))
segundo_valor = int(input("Ingrese el segundo valor: "))
resultado = sumar_valores(primer_valor, segundo_valor)
print(resultado)

# PIDE LA EDAD DEL EJERCICIO 4 Y USA LA FUNCION DE JUBILACION
edad = int(input("Ingrese su edad: "))
mensaje = verificar_jubilacion(edad)
print(mensaje)