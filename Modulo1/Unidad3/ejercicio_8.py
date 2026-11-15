"""
Ejercicio 8 escalable (M1-U3)
A partir del ejercicio 6 cree un programa con 4 funciones:
alta() para dar de alta la nueva compra
baja() para dar de baja una compra
consulta() para consultar por todas las compras realizadas hasta el momento
modificar() para modificar una compra realizada
Versión con separación modelo-vista-controlador.
"""

# MODELO: Calcula el subtotal de un producto
def calcular_subtotal(cantidad, precio):
    return cantidad * precio

# ALTA: Pide los datos de una compra, la agrega a la lista y devuelve la lista
def alta(compras):
    cantidad = float(input("Ingrese la cantidad de productos: "))
    precio = float(input("Ingrese el precio del producto: "))
    subtotal = calcular_subtotal(cantidad, precio)
    compras.append([cantidad, precio, subtotal])
    print("Compra agregada exitosamente")
    return compras

# BAJA: elimina una compra elegida por su número y devuelve la lista
def baja(compras):
    if len(compras) == 0:
        print("No hay compras para dar de baja.")
        return compras
    consulta(compras)
    numero = int(input("Ingrese el numero de la compra a dar de baja: "))
    if numero >= 1 and numero <= len(compras):
        del compras[numero - 1]
        print("Compra dada de baja correctamente.")
    else:
        print("Numero invalido.")
    return compras

# CONSULTA: Muestra todas las compras cargadas con su numero
def consulta(compras):
    if len(compras) == 0:
        print("No hay compras cargadas")
        return compras
    for indice, compra in enumerate(compras):
        numero = indice + 1
        print(f"{numero}) Cantidad: {compra[0]} - Precio: ${compra[1]:.2f} - Subtotal: ${compra[2]:.2f}")
    return compras

# MODIFICAR: Reemplaza los datos de una compra elegida por su numero
def modificar(compras):
    if len(compras) == 0:
        print("No hay compras para modificar.")
        return compras
    consulta(compras)
    numero = int(input("Ingrese el numero de la compra a modificar: "))
    if numero >= 1 and numero <= len(compras):
        cantidad = float(input("Ingrese la nueva cantidad: "))
        precio = float(input("Ingrese el nuevo precio: "))
        subtotal = calcular_subtotal(cantidad, precio)
        compras[numero - 1] = [cantidad, precio, subtotal]
        print("Compra modificada correctamente.")
    else:
        print("Numero invalido.")
    return compras

# CONTROLADOR: Muestra el menu y coordina las operaciones
def menu():
    compras = []
    opcion = ""
    while opcion != "5":
        print("--- Menu ---")
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
            print("Opcion Invalida")

menu()