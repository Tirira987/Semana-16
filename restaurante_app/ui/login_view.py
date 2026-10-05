import tkinter as tk
from tkinter import ttk
from pathlib import Path


class LoginView(ttk.Frame):

    def __init__(
        self,
        parent,
        restaurante_servicio,
        on_login_success
    ):

        super().__init__(parent)

        self.restaurante_servicio = (
            restaurante_servicio
        )

        self.on_login_success = (
            on_login_success
        )

        self.logo = None

        self.crear_interfaz()

    def crear_interfaz(self):

        contenedor = ttk.Frame(self)

        contenedor.pack(
            expand=True
        )

        # =====================================
        # LOGO
        # =====================================

        try:

            ruta_logo = (
                Path(__file__).resolve().parent.parent
                / "assets"
                / "logo"
                / "logo.png"
            )
            self.logo = tk.PhotoImage(
                file=str(ruta_logo)
            )

            logo_label = ttk.Label(
                contenedor,
                image=self.logo
            )

            logo_label.pack(
                pady=(20, 10)
            )

        except Exception:

            ttk.Label(
                contenedor,
                text="RESTAURANTE APP",
                font=("Arial", 24, "bold")
            ).pack(
                pady=20
            )

        # =====================================
        # TITULO
        # =====================================

        ttk.Label(
            contenedor,
            text="Inicio de sesión",
            font=("Arial", 16, "bold")
        ).pack(
            pady=10
        )

        # =====================================
        # USUARIO
        # =====================================

        ttk.Label(
            contenedor,
            text="Usuario:"
        ).pack(
            pady=(15, 5)
        )

        self.entrada_usuario = ttk.Entry(
            contenedor,
            width=30
        )

        self.entrada_usuario.pack()

        # =====================================
        # CONTRASEÑA
        # =====================================

        ttk.Label(
            contenedor,
            text="Contraseña:"
        ).pack(
            pady=(15, 5)
        )

        self.entrada_contrasena = ttk.Entry(
            contenedor,
            width=30,
            show="*"
        )

        self.entrada_contrasena.pack()

        # =====================================
        # MENSAJE
        # =====================================

        self.mensaje = ttk.Label(
            contenedor,
            text=""
        )

        self.mensaje.pack(
            pady=10
        )

        # =====================================
        # BOTÓN
        # =====================================

        ttk.Button(
            contenedor,
            text="Ingresar",
            command=self.iniciar_sesion
        ).pack(
            pady=10
        )

        # =====================================
        # DATOS DE PRUEBA
        # =====================================

        ttk.Label(
            contenedor,
            text="Usuario: richi   Contraseña: 6666"
        ).pack(
            pady=5
        )

        ttk.Label(
            contenedor,
            text="Usuario: maria   Contraseña: 1234"
        ).pack()

        self.entrada_usuario.focus()
        self.entrada_contrasena.bind("<Return>", lambda event: self.iniciar_sesion())

    def iniciar_sesion(self):

        nombre_usuario = (
            self.entrada_usuario
            .get()
            .strip()
        )

        contrasena = (
            self.entrada_contrasena
            .get()
        )

        if (
            not nombre_usuario
            or not contrasena
        ):

            self.mensaje.config(
                text=(
                    "Ingrese usuario "
                    "y contraseña."
                )
            )

            return

        usuario = (
            self.restaurante_servicio
            .validar_acceso(
                nombre_usuario,
                contrasena
            )
        )

        if usuario is not None:

            self.on_login_success(
                usuario
            )

        else:

            self.mensaje.config(
                text=(
                    "Usuario o contraseña "
                    "incorrectos."
                )
            )

            self.entrada_contrasena.delete(
                0,
                tk.END
            )

            self.entrada_contrasena.focus()