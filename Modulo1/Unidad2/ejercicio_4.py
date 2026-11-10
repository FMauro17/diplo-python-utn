"""
Ejercicio 4 (M1-U2)
Realice un programa que consulte la edad y en caso de que el valor
ingresado supere la fecha de jubilación, presente en la terminal el mensaje
"Ya está en edad de jubilarse", en caso contrario que presente
"Aún está en edad de trabajar".
"""

# DEFINE LA EDAD DE JUBILACION COMO CONSTANTE
EDAD_JUBILACION = 65

# PIDE SI LA EDAD ALCANZA O SUPERA LA EDAD DE JUBILACION
edad = int(input("Ingrese su edad: "))

# EVALUA SI LA EDAD ALCANZA O SUPERA LA EDAD DE JULILACION
if edad >= EDAD_JUBILACION:
    print("Ya esta en edad de jubilarse")
else:
    print("Aun esta en edad de trabajar")