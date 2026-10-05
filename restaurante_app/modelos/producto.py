class Producto:

    def __init__(
        self,
        id_producto: int,
        nombre: str,
        precio: float,
        categoria: str,
        stock: int
    ):

        if (
            not isinstance(id_producto, int)
            or id_producto <= 0
        ):
            raise ValueError(
                "El ID debe ser un entero positivo."
            )

        if not nombre or not nombre.strip():
            raise ValueError(
                "El nombre es obligatorio."
            )

        if precio <= 0:
            raise ValueError(
                "El precio debe ser mayor que cero."
            )

        if not categoria or not categoria.strip():
            raise ValueError(
                "La categoría es obligatoria."
            )

        if (
            not isinstance(stock, int)
            or stock < 0
        ):
            raise ValueError(
                "El stock debe ser un entero "
                "mayor o igual a cero."
            )

        self.id_producto = id_producto
        self.nombre = nombre
        self.precio = precio
        self.categoria = categoria
        self.stock = stock

    @classmethod
    def desde_diccionario(cls, datos: dict):

        return cls(
            datos["id_producto"],
            datos["nombre"],
            datos["precio"],
            datos["categoria"],
            datos["stock"]
        )

    def a_diccionario(self) -> dict:

        return {
            "id_producto": self.id_producto,
            "nombre": self.nombre,
            "precio": self.precio,
            "categoria": self.categoria,
            "stock": self.stock
        }

    def __str__(self):

        return (
            f"{self.id_producto} - "
            f"{self.nombre} - "
            f"${self.precio:.2f} - "
            f"{self.categoria} - "
            f"Stock: {self.stock}"
        )