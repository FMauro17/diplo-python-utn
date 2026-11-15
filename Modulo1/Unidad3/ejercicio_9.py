"""
Ejercicio 9 escalable (M1-U3)
A partir del ejercicio 7 cree un programa con 4 funciones:
alta() para dar de alta la nueva compra
baja() para dar de baja una compra
consulta() para consultar por todas las compras realizadas hasta el momento
modificar() para modificar una compra realizada
Versión con separación modelo-vista-controlador.
"""

# MODELO: Calcula el subtotal de un producto
def calcular_subtotal(cantidad, precio):
    return cantidad * precio

# ALTA: Pide los datos de una compra, la agrega al diccionario y lo devuelve
def alta(compras):
    cantidad = float(input("Ingrese la cantidad de productos: "))
    precio = float(input("Ingrese el precio del producto: "))
    subtotal = calcular_subtotal(cantidad, precio)
    if len(compras) == 0:
        numero_nuevo = 1
    else:
        numero_nuevo = max(compras) + 1
    compras[numero_nuevo] = {"cantidad": cantidad, "precio": precio, "subtotal": subtotal}
    print("Compra agregada correctamente.")
    return compras

# BAJA: Elimina una compra elegida por su numero y devuelve el diccionario
def baja(compras):
    if len(compras) == 0:
        print("No hay compras para dar de baja.")
        return compras
    consulta(compras)
    numero = int(input("Ingrese el numero de la compra a dar de baja: "))
    if numero in compras:
        del compras[numero]
        print("Compra dada de baja correctamente.")
    else:
        print("Numero invalido.")
    return compras

# CONSULTA: Muestra todas las compras cargadas con su numero
def consulta(compras):
    if len(compras) == 0:
        print("No hay compras cargadas")
        return compras
    for numero, datos in compras.items():
        print(f"{numero}) Cantidad: {datos['cantidad']} - Precio: ${datos['precio']:.2f} - Subtotal: ${datos['subtotal']:.2f}")
    return compras

# MODIFICAR: Reemplaza los datos de una compra elegida por su numero
def modificar(compras):
    if len(compras) == 0:
        print("No hay compras para modificar.")
        return compras
    consulta(compras)
    numero = int(input("Ingrese el numero de la compra a modificar: "))
    if numero in compras:
        cantidad = float(input("Ingrese la nueva cantidad: "))
        precio = float(input("Ingrese el nuevo precio: "))
        subtotal = calcular_subtotal(cantidad, precio)
        compras[numero] = {"cantidad": cantidad, "precio": precio, "subtotal": subtotal}
        print("Compra modificada correctamente.")
    else:
        print("Numero invalido.")
    return compras

# CONTROLADOR: Muestra el menu y coordina las operaciones
def menu():
    compras = {}
    opcion = ""
    while opcion != "5":
        print("---Menu---")
        print("1: Alta")
        print("2: Baja")
        print("3: Consulta")
        print("4: Modificar")
        print("5: Salir")
        opcion = input("Elija una opcion: ")
        if opcion == "1":
            compras = alta(compras)
        elif opcion == "2":
            compras = baja(compras)
        elif opcion == "3":
            compras = consulta(compras)
        elif opcion == "4":
            compras = modificar(compras)
        elif opcion == "5":
            print("Programa finalizado.")
        else:
            print("Opcion invalida.")

menu()