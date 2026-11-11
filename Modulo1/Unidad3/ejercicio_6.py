"""
Ejercicio 6 (M1-U3)
A partir del ejercicio 5 cree un programa que vaya agregando en una
lista las compras realizadas.
"""

# Toma los productos de a uno y devuelve una lista con cada compra realizada
def cargar_compras():
    # Inicializa la lista que almacena los compras
    compras = []
    # Controla la continuidad del bucle
    continuar = "si"
    # Repite mientras el cliente quiera seguir cargando productos
    while continuar == "si":
        # Pide la cantidad y el precio del producto actual
        cantidad = float(input("Ingrese la cantidad de productos: "))
        precio = float(input("Ingrese el precio del producto: "))
        # Calcula el subtotal del producto
        subtotal = cantidad * precio
        # Agrega el producto a la lista como [cantidad, precio, subtotal]
        compras.append([cantidad, precio, subtotal])
        # Pregunta si el cliente desea cargar otro producto
        continuar = input("Desea cargar otro producto? (si/no): ").lower()
    # Devuelve la lista con todas las compras
    return compras

# Ejecuta la carga y guarda la lista de compras devuelta
lista_compras = cargar_compras()

# Inicializa el acumulador del total
total = 0

# Recorre cada compra de la lista y muestra su detalle
for compra in lista_compras:
    # Accede a los tres valores de la compra por su posicion
    cantidad = compra[0]
    precio = compra[1]
    subtotal = compra[2]
    # Muestra el detalle del producto
    print(f"Cantidad: {cantidad}, Precio: ${precio:.2f}, Subtotal: ${subtotal:.2f}")
    # Suma el subtotal al total
    total += subtotal

# Muestra el monto total gastado
print(f"El monto total gastado es: ${total:.2f}")