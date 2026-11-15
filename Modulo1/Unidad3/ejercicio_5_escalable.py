"""
Ejercicio 5.1 (M1-U3) - Versión escalable
Suponga que tiene una verdulería y carga la cantidad y el precio de lo
comprado por un cliente. Realice un programa que tome de a uno la cantidad y el
precio comprado por el cliente y al finalizar la compra retorne el monto total
gastado.
Esta versión separa la lógica (modelo), la interfaz (vista) y la coordinación
(controlador) para que el código sea escalable.
"""

# MODELO: Logica pura, sin input ni print
# Calcula el subtotal de un producto a partir de su cantidad y precio
def calcular_subtotal(cantidad, precio):
    return cantidad * precio

# VISTA: Pide al usuario la cantidad y el precio y los devuelve
def pedir_producto():
    cantidad = float(input("Ingrese la cantidad de productos: "))
    precio = float(input("Ingrese el precio del producto: "))
    return cantidad, precio

# VISTA: Pregunta si desea cargar otro producto y devuelve la respuesta
def preguntar_continuar():
    return input("Desea cargar otro producto? (si/no): ").lower()

# VISTA: Muestra el monto total gastado
def mostrar_total(total):
    print(f"El monto total gastado es: ${total:.2f}")

# CONTROLADOR: Coordina el modelo y la vista, y devuelve el total gastado
def gestionar_compra():
    total = 0
    continuar = "si"
    while continuar == "si":
        cantidad, precio = pedir_producto()
        total += calcular_subtotal(cantidad, precio)
        continuar = preguntar_continuar()
    return total

# Punto de entrada: ejecuta el controlador y muestra el resultado
total_compra = gestionar_compra()
mostrar_total(total_compra)