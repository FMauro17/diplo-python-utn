"""
Ejercicio 1 (Este es el ejercicio 2 de la unidad 1 pero implementando if/else
Cree un programa que incorpore el módulo sys, al cual desde la terminal se le puedan
pasar tres parámetros. El programa debe tomar los parámetros e indicar en la terminal si
son multiplos de 2.
Utilice la estructura if/else
"""

# IMPORTA EL MODULO SYS PARA ACCEDER A LOS PAREMETROS QUE SE PASAN DESDE LA TERMINAL
import sys

# VERIFICA QUE SE HAYA PASADO EXATAMENTE TRES PAREMTROS
# SYS.ARGV[0] GUARDA EL NOMBRE DEL SCRIPT, POR ESO EL TOTAL ESPERADO ES 4 
if len(sys.argv) == 4:
    # CONVIERTE CADA PARAMETRO DE TEXTO A NUMERO ENTERO
    primer_numero = int(sys.argv[1])
    segundo_numero = int(sys.argv[2])
    tercer_numero = int(sys.argv[3])

    # EVALUA SI EL PRIMER NUMERO ES MULTIPLO DE 2
    if primer_numero % 2 == 0:
        print(f"{primer_numero} es multiplo de 2")
    else:
        print(f"{primer_numero} no es multiplo de 2")

    # EVALUA SI EL SEGUNDO NUMERO ES MULTIPLO DE 2
    if segundo_numero % 2 == 0:
        print(f"{segundo_numero} es multiplo de 2")
    else:
        print(f"{segundo_numero} no es multiplo de 2")

    # EVALUA SI EL TERCER NUMERO ES MULTIPLO DE 2
    if tercer_numero % 2 == 0:
        print(f"{tercer_numero} es multiplo de 2")
    else:
        print(f"{tercer_numero} no es multiplo de 2")
else:
    # AVISA QUE LA CANTIDAD DE PARAMETROS NO ES LA CORRECTA
    print("Error: se deben pasar exactamente tres parametros")