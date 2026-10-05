import json
from pathlib import Path

from modelos.producto import Producto
from modelos.usuario import Usuario
from modelos.venta import Venta


class ArchivoServicio:

    def __init__(self):
        self.ruta_datos = Path(__file__).resolve().parent.parent / "datos"

    def _cargar_datos(self, nombre_archivo):
        ruta = self.ruta_datos / nombre_archivo
        try:
            with open(ruta, "r", encoding="utf-8") as archivo:
                return json.load(archivo)
        except FileNotFoundError:
            raise FileNotFoundError(f"No se encontró el archivo: {ruta}")
        except json.JSONDecodeError:
            raise ValueError(f"El archivo {nombre_archivo} no contiene JSON válido.")

    def _guardar_datos(self, nombre_archivo, datos):
        ruta = self.ruta_datos / nombre_archivo
        self.ruta_datos.mkdir(parents=True, exist_ok=True)
        with open(ruta, "w", encoding="utf-8") as archivo:
            json.dump(datos, archivo, ensure_ascii=False, indent=4)

    def cargar_productos(self):
        datos = self._cargar_datos("productos.json")
        return [Producto.desde_diccionario(producto) for producto in datos]

    def cargar_usuarios(self):
        datos = self._cargar_datos("usuarios.json")
        return [Usuario.desde_diccionario(usuario) for usuario in datos]

    def cargar_ventas(self):
        datos = self._cargar_datos("ventas.json")
        return [Venta.desde_diccionario(venta) for venta in datos]

    def guardar_productos(self, productos):
        self._guardar_datos("productos.json", [producto.a_diccionario() for producto in productos])

    def guardar_usuarios(self, usuarios):
        self._guardar_datos("usuarios.json", [usuario.a_diccionario() for usuario in usuarios])

    def guardar_ventas(self, ventas):
        self._guardar_datos("ventas.json", [venta.a_diccionario() for venta in ventas])
