"""
Ejercicio 7 escalable (M1-U3)
A partir del ejercicio 5 cree un programa que vaya agregando en un
diccionario las compras realizadas.
Versión con separación modelo-vista-controlador.
"""

# MODELO: Calcula el subtotal de un producto
def calcular_subtotal(cantidad, precio):
    return cantidad * precio

# MODELO: Recibe el diccionario de compras y devuelve la suma de los subtotales
def calcular_total(compras):
    total = 0
    for datos in compras.values():
        total += datos["subtotal"]
    return total

# VISTA: Pide la cantidad y el precio de un producto y los devuelve
def pedir_producto():
    cantidad = float(input("Ingrese la cantidad de productos: "))
    precio = float(input("Ingrese el precio del producto: "))
    return cantidad, precio

# VISTA: Muestra si desea cargar otro producto y devuelve la respuestas
def preguntar_continuar():
    return input("¿Desea cargar otro producto? (si/no): ").lower()

# VISTA: Muestra el detalle de cada compra del diccionario
def mostrar_compras(compras):
    for numero, datos in compras.items():
        cantidad = datos["cantidad"]
        precio = datos["precio"]
        subtotal = datos["subtotal"]
        print(f"Producto {numero} - Cantidad: {cantidad} - Precio: ${precio:.2f} - Subtotal: ${subtotal:.2f}")

# VISTA: Muestra el monto total gastado
def mostrar_total(total):
    print(f"El monto total gastado es ${total:.2f}")

# CONTROLADOR: Coordina la carga y devuelve el diccionario de compras
def gestionar_compras():
    compras = {}
    numero_producto = 1
    continuar = "si"
    while continuar == "si":
        cantidad, precio = pedir_producto ()
        subtotal = calcular_subtotal(cantidad, precio)
        compras[numero_producto] = {
            "cantidad": cantidad,
            "precio": precio,
            "subtotal": subtotal,
        }
        numero_producto += 1
        continuar = preguntar_continuar()
    return compras

# Punto de entreda: ejecuta el controlador y muestra los resultados
dic_compras = gestionar_compras()
mostrar_compras(dic_compras)
total_compras = calcular_total(dic_compras)
mostrar_total(total_compras)