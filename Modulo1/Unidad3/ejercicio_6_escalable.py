"""
Ejercicio 6 escalable (M1-U3)
A partir del ejercicio 5 cree un programa que vaya agregando en una
lista las compras realizadas.
Versión con separación modelo-vista-controlador.
"""

# MODELO: Calcula el subtotal de un producto
def calcular_subtotal(cantidad, precio):
    return cantidad * precio

# MODELO: Recibe la lista de compras y devuelve la suma de todos los subtotales
def calcular_total(compras):
    total = 0
    for compra in compras:
        total += compra[2] # El subtotal está en la posición 2 de cada compra
    return total

# VISTA: Pide la cantidad y el precio de un producto y los devuelve
def pedir_producto():
    cantidad = float(input("Ingrese la cantidad de productos: "))
    precio = float(input("Ingrese el precio del producto: "))
    return cantidad, precio 

# VISTA: Pregunta si desea cargar otro producto y devuelve la respuesta
def preguntar_continuar():
    return input("Desea cargar otro producto? (si/no): ").lower()

# VISTA: Muestra el detalle de cada compra de la lista
def mostrar_compras(compras):
    for compra in compras:
        cantidad = compra[0]
        precio = compra[1]
        subtotal = compra[2]
        print(f"Cantidad: {cantidad} - Precio: ${precio:.2f} - Subtotal: ${subtotal:.2f}")

# VISTA: Muestra el monto total gastado
def mostrar_total(total):
    print(f"El monto total gastado es: {total:.2f}")

# CONTROLADOR: Controla la carga y devuelve la lista de compras
def gestionar_compras():
    compras = []
    continuar = "si"
    while continuar == "si":
        cantidad, precio = pedir_producto()
        subtotal = calcular_subtotal(cantidad, precio)
        compras.append([cantidad, precio, subtotal])
        continuar = preguntar_continuar()
    return compras

# Punto de entrada: Ejecuta el controlador y muestra los resultados
lista_compras = gestionar_compras()
mostrar_compras(lista_compras)
total_compra = calcular_total(lista_compras)
mostrar_total(total_compra) 