"""
Ejercicio 5 (M1-U3)
Suponga que tiene una verdulería y carga la cantidad y el precio de lo
comprado por un cliente. Realice un programa que tome de a uno la cantidad y el
precio comprado por el cliente y al finalizar la compra retorne el monto total
gastado.
"""

# Toma los productos de a uno y devuelve el monto total de la compra
def cargar_compra():
    # Inicializa el acumulador del total
    total = 0
    # Controla la continuidad  del bucle; arranca en "s" para entrar al menos una vez
    continuar = "si"
    # Repite mientras el cliente quiera seguir cargando productos
    while continuar == "si":
        # Pide la cantidad y el precio del producto actual
        cantidad = float(input("Ingrese la cantidad de productos: "))
        precio = float(input("Ingrese el precio del producto: "))
        # Suma al subtotal del producto al total acumulado
        total += cantidad * precio
        # Pregunta si el cliente desea cargar otro producto
        continuar = input("Desea cargar otro producto? (si/no): ").lower()
    # Devuelve el monto total de la compra
    return total

# Ejecuta la carga de la compra y guarda el total devuelto
total_compra = cargar_compra()

# Muestra el monto total gastado
print(f"El monto total gastado es: ${total_compra:.2f}")