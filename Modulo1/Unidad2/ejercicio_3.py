"""
Ejercicio 3 (M1-U2)
Tome dos valores por consola, y guarde en una lista:
[primer_valor, segundo_valor, la_suma_de_los_valores].
Presente el resultado en la terminal del editor.
"""

# PIDE EL PRIMER VALOR POR CONSOLA Y LO CONVIERTE A ENTERO
primer_valor = int(input("Ingrese el primer valor: "))

# PIDE EL SEGUNDO VALOR POR CONSOLA Y LO CONVIERTE A ENTERO
segundo_valor = int(input("Ingrese el segundo valor: "))

# ARMA UNA LISTA CON LOS 2 VALORES Y SU SUMA
resultado = [primer_valor, segundo_valor, primer_valor + segundo_valor]

# MUESTRA LA LISTA EN LA TERMINAL
print(resultado)