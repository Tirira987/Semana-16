from datetime import datetime


class Venta:

    def __init__(self, id_venta, id_usuario, id_producto, fecha):
        if int(id_venta) <= 0:
            raise ValueError("El ID de venta debe ser mayor que 0.")
        if int(id_usuario) <= 0:
            raise ValueError("El ID de usuario debe ser mayor que 0.")
        if int(id_producto) <= 0:
            raise ValueError("El ID de producto debe ser mayor que 0.")
        if not str(fecha).strip():
            raise ValueError("La fecha es obligatoria.")

        self.id_venta = int(id_venta)
        self.id_usuario = int(id_usuario)
        self.id_producto = int(id_producto)
        self.fecha = str(fecha)

    @classmethod
    def desde_diccionario(cls, datos):
        return cls(
            datos["id_venta"],
            datos["id_usuario"],
            datos["id_producto"],
            datos["fecha"]
        )

    def a_diccionario(self):
        return {
            "id_venta": self.id_venta,
            "id_usuario": self.id_usuario,
            "id_producto": self.id_producto,
            "fecha": self.fecha
        }

    @classmethod
    def crear(cls, id_venta, id_usuario, id_producto):
        fecha = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        return cls(id_venta, id_usuario, id_producto, fecha)

    def __str__(self):
        return f"Venta {self.id_venta} - Usuario {self.id_usuario} - Producto {self.id_producto} - {self.fecha}"
