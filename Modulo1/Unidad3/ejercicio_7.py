"""
Ejercicio 7 (M1-U3)
A partir del ejercicio 5 cree un programa que vaya agregando en un
diccionario las compras realizadas.
"""

# Toma los productos de a uno y devuelve un diccionario con cada compra realizada
def cargar_compras():
    # Inicializa el diccionario que almacena las compras
    compras = {}
    # Lleva el numero de producto, que se usa como clave
    numero_producto = 1
    # Controla la continuidad del bucle 
    continuar = "si"
    # Repite mientras el cliente quiera seguir cargando productos
    while continuar == "si":
        # Pide la cantidad y el precio del producto actual
        cantidad = float(input("Ingrese la cantidad de productos: "))
        precio = float(input("Ingrese el precio del producto: "))
        # Calcula el subtotal del producto
        subtotal = cantidad * precio
        # Agrega el producto al diccionario con sus datos nombrados
        compras[numero_producto] = {
            "cantidad": cantidad,
            "precio": precio,
            "subtotal": subtotal,
        }
        # Incrementa el numero de producto para la proxima compra
        numero_producto += 1
        # # Pregunta si el cliente desea cargar otro producto
        continuar = input("Desea cargar otro producto? (si/no): ").lower()
    # devuelve el diccionario con todas las compras
    return compras

# Ejecuta la carga y guarda el diccionario de compras devuelto
dic_compras = cargar_compras()

# Inicializa el acumulador del total
total = 0

# Recorre cada compra del diccionario y muestra su detalle
for numero, datos in dic_compras.items():
    # Accede a cada dato por su nombre
    cantidad = datos["cantidad"]
    precio = datos["precio"]
    subtotal = datos["subtotal"]
    # Muestra el detalle del producto
    print(f"Producto {numero} - Cantidad: {cantidad} - Precio: ${precio:.2f} - Subtotal: ${subtotal:.2f}")
    # Suma el subtotal al total
    total += subtotal

# Muestra el monto total gastado
print(f"El monto total gastado es: ${total:.2f}")