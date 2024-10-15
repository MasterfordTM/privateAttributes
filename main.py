from classVenta import Venta

venta = Venta()

Venta.set_id_venta(1)
Venta.set_fecha("15/10/2024")
Venta.set_cliente("cesar ")
Venta.set_productos(["producto1 , producto2 , producto3"])
Venta.set_total(150.75)

Venta.mostrar_detalle()