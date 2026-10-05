from typing import Optional

from modelos.producto import Producto
from modelos.usuario import Usuario
from modelos.venta import Venta


class RestauranteServicio:

    def __init__(self, productos, usuarios, archivo_servicio, ventas=None):
        self._productos = productos
        self._usuarios = usuarios
        self._archivo_servicio = archivo_servicio
        self._ventas = ventas if ventas is not None else []
        self._actualizar_indices()

    def _actualizar_indices(self):
        self._indice_productos = {p.id_producto: p for p in self._productos}
        self._indice_usuarios = {u.id_usuario: u for u in self._usuarios}

    def validar_acceso(self, nombre_usuario: str, contrasena: str) -> Optional[Usuario]:
        for usuario in self._usuarios:
            if usuario.nombre_usuario == nombre_usuario and usuario.contrasena == contrasena:
                return usuario
        return None

    def listar_usuarios(self):
        return list(self._usuarios)

    def buscar_usuario(self, id_usuario):
        return self._indice_usuarios.get(id_usuario)

    def obtener_cantidad_usuarios(self):
        return len(self._usuarios)

    def agregar_usuario(self, id_usuario, nombre, rol, nombre_usuario, contrasena):
        if rol == "Administrador":
            raise ValueError("No se pueden registrar nuevos usuarios Administrador.")
        if self.buscar_usuario(id_usuario) is not None:
            raise ValueError("Ya existe un usuario con ese ID.")
        if any(u.nombre_usuario.lower() == nombre_usuario.strip().lower() for u in self._usuarios):
            raise ValueError("Ya existe un usuario con ese nombre de usuario.")
        usuario = Usuario(id_usuario, nombre, rol, nombre_usuario, contrasena)
        self._usuarios.append(usuario)
        self._actualizar_indices()
        self.guardar_usuarios()
        return usuario

    def actualizar_usuario(self, id_usuario, nombre, rol, nombre_usuario, contrasena):
        usuario = self.buscar_usuario(id_usuario)
        if usuario is None:
            raise ValueError("No se encontró el usuario.")
        if rol == "Administrador" and usuario.rol != "Administrador":
            raise ValueError("No se puede asignar el rol Administrador a otro usuario.")
        if any(u.id_usuario != id_usuario and u.nombre_usuario.lower() == nombre_usuario.strip().lower() for u in self._usuarios):
            raise ValueError("Ya existe otro usuario con ese nombre de usuario.")
        usuario.nombre = nombre.strip()
        usuario.rol = rol
        usuario.nombre_usuario = nombre_usuario.strip()
        usuario.contrasena = contrasena
        # Validar el objeto completo con las mismas reglas del modelo.
        Usuario(usuario.id_usuario, usuario.nombre, usuario.rol, usuario.nombre_usuario, usuario.contrasena)
        self._actualizar_indices()
        self.guardar_usuarios()
        return usuario

    def eliminar_usuario(self, id_usuario, id_usuario_actual=None):
        if id_usuario_actual is not None and id_usuario == id_usuario_actual:
            raise ValueError("No puede eliminar la cuenta administrativa con la que está iniciada la sesión.")
        usuario = self.buscar_usuario(id_usuario)
        if usuario is None:
            raise ValueError("No se encontró el usuario.")
        self._usuarios.remove(usuario)
        self._actualizar_indices()
        self.guardar_usuarios()

    def guardar_usuarios(self):
        self._archivo_servicio.guardar_usuarios(self._usuarios)

    def listar_productos(self):
        return list(self._productos)

    def buscar_producto(self, id_producto):
        return self._indice_productos.get(id_producto)

    def obtener_cantidad_productos(self):
        return len(self._productos)

    def agregar_producto(self, id_producto, nombre, precio, categoria, stock):
        if self.buscar_producto(id_producto) is not None:
            raise ValueError("Ya existe un producto con ese ID.")
        producto = Producto(id_producto, nombre, precio, categoria, stock)
        self._productos.append(producto)
        self._actualizar_indices()
        self.guardar_productos()
        return producto

    def actualizar_producto(self, id_producto, nombre, precio, categoria, stock):
        producto = self.buscar_producto(id_producto)
        if producto is None:
            raise ValueError("No se encontró el producto.")
        producto.nombre = nombre
        producto.precio = precio
        producto.categoria = categoria
        producto.stock = stock
        self._actualizar_indices()
        self.guardar_productos()
        return producto

    def eliminar_producto(self, id_producto):
        producto = self.buscar_producto(id_producto)
        if producto is None:
            raise ValueError("No se encontró el producto.")
        self._productos.remove(producto)
        self._actualizar_indices()
        self.guardar_productos()

    def guardar_productos(self):
        self._archivo_servicio.guardar_productos(self._productos)

    # ==========================================
    # VENTAS
    # ==========================================

    def listar_ventas(self):
        return list(self._ventas)

    def obtener_cantidad_ventas(self):
        return len(self._ventas)

    def registrar_venta(self, id_usuario, id_producto):
        usuario = self.buscar_usuario(id_usuario)
        if usuario is None:
            raise ValueError("No se encontró el usuario seleccionado.")

        producto = self.buscar_producto(id_producto)
        if producto is None:
            raise ValueError("No se encontró el producto seleccionado.")

        if producto.stock <= 0:
            raise ValueError("El producto no tiene stock disponible.")

        nuevo_id = max((venta.id_venta for venta in self._ventas), default=0) + 1
        venta = Venta.crear(nuevo_id, id_usuario, id_producto)
        self._ventas.append(venta)
        producto.stock -= 1
        self._actualizar_indices()
        self.guardar_productos()
        self.guardar_ventas()
        return venta

    def guardar_ventas(self):
        self._archivo_servicio.guardar_ventas(self._ventas)
