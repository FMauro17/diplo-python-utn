"""
Ejercicio 1 (M1-U3)
Tome el ejercicio de cálculo de números pares e impares de la unidad 2
y agréguele un bucle al código de forma de simplificarlo.
"""

import sys

# VERIFICA QUE SE HAYA PASADO AL MENOS UN PARAMETRO
if len(sys.argv) > 1:
    # RECORRE CADA PARAMETRO RECIBIDO DESDE LA TERMINAL, OMITIENDO EL NOMBRE DEL SCRIPT
    for parametro in sys.argv[1:]:
        # CONVIERTE EL PARAMETRO DE TEXTO A NUMERO ENTERO 
        numero = int(parametro)
        # EVALUA SI EL NUMERO ES MULTIPLO DE 2    
        if numero % 2 == 0:         
            print(f"{numero} es multiplo de 2")
        else:
            print(f"{numero} no es multiplo de 2")
else:
    # AVISA QUE NO SE RECIBIERON PARAMETROS
    print("Error: se debe pasar al menos un parametro")