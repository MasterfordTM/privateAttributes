class Venta:
    __id_venta = None
    __fecha = None
    __cliente = None
    __productos = None
    __total = 0.0

    # Getters para acceder a los atributos privados
    def get_id_venta(self):
        return self.__id_venta

    def get_fecha(self):
        return self.__fecha

    def get_cliente(self):
        return self.__cliente

    def get_productos(self):
        return self.__productos

    def get_total(self):
        return self.__total

    # Setters para modificar los atributos privados
    def set_id_venta(self, id_venta):
        self.__id_venta = id_venta

    def set_fecha(self, fecha):
        self.__fecha = fecha

    def set_cliente(self, cliente):
        self.__cliente = cliente

    def set_productos(self, productos):
        self.__productos = productos
        self.__calcular_total()  # Calcula el total automáticamente

    # Método para calcular el total
    def __calcular_total(self):
        self.__total = sum(
            producto['cantidad'] * producto['precio_unitario'] for producto in self.__productos
        )

    # Método para mostrar los detalles de la venta
    def mostrar_detalle(self):
        print(f"ID Venta: {self.__id_venta}")
        print(f"Fecha: {self.__fecha}")
        print(f"Cliente: {self.__cliente}")
        print(f"Productos:")
        for producto in self.__productos:
            print(f" - Producto: {producto['producto']}, Cantidad: {producto['cantidad']}, Precio Unitario: {producto['precio_unitario']}")
        print(f"Total: ${self.__total:.2f}")