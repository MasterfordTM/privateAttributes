from classVenta import Venta

venta = Venta()


productos = []


productos_permitidos = ['Producto A', 'Producto B', 'Producto C']


for producto in productos_permitidos:
    cantidad = int(input(f"Ingrese la cantidad para {producto}: "))
    precio_unitario = float(input(f"Ingrese el precio unitario para {producto}: "))


    producto_dict = {
        "producto": producto,
        "cantidad": cantidad,
        "precio_unitario": precio_unitario
    }

    productos.append(producto_dict)


venta.set_id_venta(1)
venta.set_fecha("15/10/2024")
venta.set_cliente("Cesar")
venta.set_productos(productos)


venta.mostrar_detalle()