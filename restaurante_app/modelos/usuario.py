class Usuario:

    ROLES_VALIDOS = ("Administrador", "Empleado", "Cliente")

    def __init__(self, id_usuario: int, nombre: str, rol: str, nombre_usuario: str, contrasena: str):
        if not isinstance(id_usuario, int) or id_usuario <= 0:
            raise ValueError("El ID debe ser un entero positivo.")
        if not nombre or not nombre.strip():
            raise ValueError("El nombre es obligatorio.")
        if rol not in self.ROLES_VALIDOS:
            raise ValueError("El rol debe ser Administrador, Empleado o Cliente.")
        if not nombre_usuario or not nombre_usuario.strip():
            raise ValueError("El usuario es obligatorio.")
        if not contrasena:
            raise ValueError("La contraseña es obligatoria.")
        self.id_usuario = id_usuario
        self.nombre = nombre.strip()
        self.rol = rol
        self.nombre_usuario = nombre_usuario.strip()
        self.contrasena = contrasena

    @classmethod
    def desde_diccionario(cls, datos: dict):
        return cls(datos["id_usuario"], datos["nombre"], datos["rol"], datos["nombre_usuario"], datos["contrasena"])

    def a_diccionario(self) -> dict:
        return {"id_usuario": self.id_usuario, "nombre": self.nombre, "rol": self.rol, "nombre_usuario": self.nombre_usuario, "contrasena": self.contrasena}

    def __str__(self):
        return f"{self.id_usuario} - {self.nombre} - {self.rol}"
