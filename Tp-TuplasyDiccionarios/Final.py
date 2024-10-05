inventario = {
    "A001": ("Placa de Video", 3000),
    "A002": ("Labial", 100),
    "A003": ("Acuario", 2000),
    "A004": ("Cuaderno", 10),
    "A005": ("Caja de regalo", 150)
}

def mostrar_inventario(inventario):
    for codigo, (descripcion, precio) in inventario.items():
        print(f"Código: {codigo}, Descripción: {descripcion}, Precio: ${precio}")

def buscar_producto(inventario, codigo):
    producto = inventario.get(codigo)
    if producto:
        descripcion, precio = producto
        print(f"Producto encontrado: {descripcion}, Precio: ${precio}")
        return True
    else:
        print("Producto NO encontrado")
        return False

def modificar_precio(inventario, codigo, nuevo_precio):
    if buscar_producto(inventario, codigo):
        descripcion = inventario[codigo][0]
        inventario[codigo] = (descripcion, nuevo_precio)
        print(f"Precio de producto modificado: {descripcion}, Nuevo precio: {nuevo_precio}")


def eliminar_producto(inventario, codigo):
    producto = inventario.pop(codigo)
    if producto:
        print(f"El producto con código {codigo} ha sido eliminado del inventario.")
    else:
        print("Producto no encontrado.")

def productos_por_rango_de_precio(inventario, min_precio, max_precio):
    print(f"Productos en el rango de precio entre ${min_precio} y ${max_precio}:")
    for codigo, (descripcion, precio) in inventario.items():
        if min_precio <= precio <= max_precio:
            print(f"Código: {codigo}, Descripción: {descripcion}, Precio: ${precio}")

mostrar_inventario(inventario)
buscar_producto(inventario, "A003")
modificar_precio(inventario, "A004", 350)
eliminar_producto(inventario, "A002")
productos_por_rango_de_precio(inventario, 100, 500)
print("")
mostrar_inventario(inventario)