"""
Ejercicio 10 (M1-U3)
Escriba un programa que guarde en una variable una contraseña y
consulte al usuario por la contraseña hasta que esta sea correcta. El programa
debe informar al usuario si la contraseña fue correcta o no.
Versión con separación modelo-vista-controlador.
"""

# MODELO: Compara la contraseña ingresada con la correcta y devuelve True o False
def es_correcta(ingresada, correcta):
    return ingresada == correcta

# VISTA: Pide la contraseña al usuario y la devuelve
def pedir_password():
    return(input("Ingrese la contraseña: "))

# VISTA: Informa que la contraseña ingresada es incorrecta
def mostrar_error():
    print("Contraseña incorrecta, intente nuevamente.")

# VISTA: Informa que la contraseña ingresada es correcta
def mostrar_exito():
    print("Contraseña correcta, acceso permitido.")

# CONTROLADOR: Pide la contraseña hasta que sea correcta
def gestionar_acceso():
    password_correcta = "python123"
    ingresada = pedir_password()
    while not es_correcta(ingresada, password_correcta):
        mostrar_error()
        ingresada = pedir_password()
    mostrar_exito()

# Punto de entrada: ejecuta el controlador
gestionar_acceso()