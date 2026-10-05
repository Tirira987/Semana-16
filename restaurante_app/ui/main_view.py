import tkinter as tk
from tkinter import ttk, messagebox
from pathlib import Path


class MainView(ttk.Frame):

    def __init__(
        self,
        parent,
        restaurante_servicio,
        usuario,
        cerrar_sesion
    ):
        super().__init__(parent)

        self.restaurante_servicio = restaurante_servicio
        self.usuario = usuario
        self.cerrar_sesion_callback = cerrar_sesion

        self.logo = None
        self.iconos = {}

        self.cargar_recursos()
        self.crear_interfaz()
        self.mostrar_inicio()

    # ==========================================
    # RECURSOS
    # ==========================================

    def cargar_recursos(self):

        self.base_dir = Path(__file__).resolve().parent.parent

        self.ruta_assets = self.base_dir / "assets"

        self.cargar_iconos()

    def cargar_iconos(self):

        nombres = [
            "home",
            "users",
            "products",
            "logout",
            "add",
            "edit",
            "delete",
            "search",
            "clean",
            "sales"
        ]

        for nombre in nombres:

            ruta = (
                self.ruta_assets
                / "icons"
                / f"{nombre}.png"
            )

            if ruta.exists():

                try:

                    self.iconos[nombre] = tk.PhotoImage(
                        file=str(ruta)
                    )

                except Exception as error:

                    print(
                        f"No se pudo cargar el icono {nombre}: {error}"
                    )

                    self.iconos[nombre] = None

            else:

                self.iconos[nombre] = None

    def obtener_icono(self, nombre):

        return self.iconos.get(nombre)

    # ==========================================
    # INTERFAZ PRINCIPAL
    # ==========================================

    def crear_interfaz(self):

        # Estilos visuales para conservar y mejorar la identidad
        # de la interfaz sin cambiar su estructura.
        estilo = ttk.Style(self)
        try:
            estilo.theme_use("clam")
        except tk.TclError:
            pass

        estilo.configure(
            "TButton",
            padding=(10, 7),
            font=("Arial", 10)
        )
        estilo.configure(
            "Treeview",
            rowheight=30,
            font=("Arial", 10)
        )
        estilo.configure(
            "Treeview.Heading",
            font=("Arial", 10, "bold")
        )
        estilo.configure(
            "TLabelframe.Label",
            font=("Arial", 10, "bold")
        )

        self.menu_lateral = ttk.Frame(
            self,
            width=190
        )

        self.menu_lateral.pack(
            side="left",
            fill="y",
            padx=(10, 0),
            pady=10
        )

        self.menu_lateral.pack_propagate(False)

        self.contenido = ttk.Frame(self)

        self.contenido.pack(
            side="left",
            fill="both",
            expand=True,
            padx=10,
            pady=10
        )

        self.crear_menu_lateral()
        self.crear_contenido()

    # ==========================================
    # MENU LATERAL
    # ==========================================

    def crear_menu_lateral(self):

        self.cargar_logo_menu()

        ttk.Label(
            self.menu_lateral,
            text=self.usuario.nombre,
            font=("Arial", 11, "bold")
        ).pack(
            pady=(5, 15)
        )

        self.crear_boton_menu(
            "Inicio",
            "home",
            self.mostrar_inicio
        )

        self.crear_boton_menu(
            "Productos",
            "products",
            self.mostrar_productos
        )

        if self.usuario.rol == "Administrador":
            self.crear_boton_menu(
                "Usuarios",
                "users",
                self.mostrar_usuarios
            )

        self.crear_boton_menu(
            "Ventas",
            "sales",
            self.mostrar_ventas
        )

        ttk.Frame(
            self.menu_lateral
        ).pack(
            fill="both",
            expand=True
        )

        self.crear_boton_menu(
            "Cerrar sesión",
            "logout",
            self.confirmar_cierre
        )

    def cargar_logo_menu(self):

        ruta_logo = (
            self.ruta_assets
            / "logo"
            / "logo.png"
        )

        if ruta_logo.exists():

            try:

                self.logo = tk.PhotoImage(
                    file=str(ruta_logo)
                )

                self.logo = self.logo.subsample(
                    3,
                    3
                )

                ttk.Label(
                    self.menu_lateral,
                    image=self.logo
                ).pack(
                    pady=(15, 5)
                )

            except Exception as error:

                print(
                    f"No se pudo cargar el logo: {error}"
                )

        else:

            print(
                f"No se encontró el logo: {ruta_logo}"
            )

    def crear_boton_menu(
        self,
        texto,
        nombre_icono,
        comando
    ):

        icono = self.obtener_icono(nombre_icono)

        if icono is not None:

            boton = ttk.Button(
                self.menu_lateral,
                text=texto,
                image=icono,
                compound="left",
                command=comando
            )

        else:

            boton = ttk.Button(
                self.menu_lateral,
                text=texto,
                command=comando
            )

        boton.pack(
            fill="x",
            padx=10,
            pady=5
        )

    # ==========================================
    # CONTENIDO
    # ==========================================

    def crear_contenido(self):

        self.titulo_contenido = ttk.Label(
            self.contenido,
            text="",
            font=("Arial", 20, "bold")
        )

        self.titulo_contenido.pack(
            anchor="w",
            pady=(5, 15)
        )

        self.panel_actual = ttk.Frame(
            self.contenido
        )

        self.panel_actual.pack(
            fill="both",
            expand=True
        )

    def limpiar_contenido(self):

        for widget in self.panel_actual.winfo_children():
            widget.destroy()

    # ==========================================
    # INICIO
    # ==========================================

    def mostrar_inicio(self):

        self.titulo_contenido.config(
            text="Inicio"
        )

        self.limpiar_contenido()

        tarjetas = ttk.Frame(
            self.panel_actual
        )

        tarjetas.pack(
            fill="x",
            pady=10
        )

        cantidad_usuarios = (
            self.restaurante_servicio
            .obtener_cantidad_usuarios()
        )

        cantidad_productos = (
            self.restaurante_servicio
            .obtener_cantidad_productos()
        )

        cantidad_ventas = (
            self.restaurante_servicio
            .obtener_cantidad_ventas()
        )

        tarjeta_usuarios = ttk.LabelFrame(
            tarjetas,
            text="Usuarios"
        )

        tarjeta_usuarios.pack(
            side="left",
            fill="both",
            expand=True,
            padx=(0, 10),
            ipadx=20,
            ipady=20
        )

        ttk.Label(
            tarjeta_usuarios,
            text=str(cantidad_usuarios),
            font=("Arial", 28, "bold")
        ).pack(
            pady=10
        )

        ttk.Label(
            tarjeta_usuarios,
            text="Usuarios registrados"
        ).pack()

        tarjeta_productos = ttk.LabelFrame(
            tarjetas,
            text="Productos"
        )

        tarjeta_productos.pack(
            side="left",
            fill="both",
            expand=True,
            padx=(10, 0),
            ipadx=20,
            ipady=20
        )

        ttk.Label(
            tarjeta_productos,
            text=str(cantidad_productos),
            font=("Arial", 28, "bold")
        ).pack(
            pady=10
        )

        ttk.Label(
            tarjeta_productos,
            text="Productos registrados"
        ).pack()

        tarjeta_ventas = ttk.LabelFrame(
            tarjetas,
            text="Ventas"
        )

        tarjeta_ventas.pack(
            side="left",
            fill="both",
            expand=True,
            padx=(10, 0),
            ipadx=20,
            ipady=20
        )

        ttk.Label(
            tarjeta_ventas,
            text=str(cantidad_ventas),
            font=("Arial", 28, "bold")
        ).pack(pady=10)

        ttk.Label(
            tarjeta_ventas,
            text="Ventas registradas"
        ).pack()

        informacion = ttk.LabelFrame(
            self.panel_actual,
            text="Información"
        )

        informacion.pack(
            fill="x",
            pady=20
        )

        ttk.Label(
            informacion,
            text=(
                "Sistema de gestión de productos "
                "del Restaurante App."
            ),
            font=("Arial", 11)
        ).pack(
            padx=15,
            pady=15
        )

    # ==========================================
    # USUARIOS
    # ==========================================

    def mostrar_usuarios(self):
        if self.usuario.rol != "Administrador":
            messagebox.showwarning("Acceso restringido", "Solo un Administrador puede gestionar usuarios.", parent=self)
            return

        self.titulo_contenido.config(text="Usuarios")
        self.limpiar_contenido()

        formulario = ttk.LabelFrame(self.panel_actual, text="Gestión de usuarios")
        formulario.pack(fill="x", padx=5, pady=5)

        ttk.Label(formulario, text="ID:").grid(row=0, column=0, padx=8, pady=8, sticky="w")
        self.entry_usuario_id = ttk.Entry(formulario, width=12)
        self.entry_usuario_id.grid(row=0, column=1, padx=8, pady=8, sticky="w")

        ttk.Label(formulario, text="Nombre:").grid(row=0, column=2, padx=8, pady=8, sticky="w")
        self.entry_usuario_nombre = ttk.Entry(formulario, width=28)
        self.entry_usuario_nombre.grid(row=0, column=3, padx=8, pady=8, sticky="w")

        ttk.Label(formulario, text="Rol:").grid(row=1, column=0, padx=8, pady=8, sticky="w")
        self.combo_usuario_rol = ttk.Combobox(formulario, values=("Empleado", "Cliente"), state="readonly", width=25)
        self.combo_usuario_rol.grid(row=1, column=1, padx=8, pady=8, sticky="w")
        self.combo_usuario_rol.bind("<<ComboboxSelected>>", self.on_rol_seleccionado)

        ttk.Label(formulario, text="Usuario:").grid(row=1, column=2, padx=8, pady=8, sticky="w")
        self.entry_usuario_nombre_usuario = ttk.Entry(formulario, width=28)
        self.entry_usuario_nombre_usuario.grid(row=1, column=3, padx=8, pady=8, sticky="w")

        ttk.Label(formulario, text="Contraseña:").grid(row=2, column=0, padx=8, pady=8, sticky="w")
        self.entry_usuario_contrasena = ttk.Entry(formulario, width=25, show="*")
        self.entry_usuario_contrasena.grid(row=2, column=1, padx=8, pady=8, sticky="w")

        ttk.Label(formulario, text="Enter: registrar | Escape: limpiar").grid(row=2, column=2, columnspan=2, padx=8, pady=8, sticky="w")

        botones = ttk.Frame(formulario)
        botones.grid(row=3, column=0, columnspan=4, padx=8, pady=10, sticky="w")
        self.crear_boton_accion_usuario(botones, "Registrar", "add", self.registrar_usuario, 0)
        self.crear_boton_accion_usuario(botones, "Actualizar", "edit", self.actualizar_usuario, 1)
        self.crear_boton_accion_usuario(botones, "Eliminar", "delete", self.eliminar_usuario, 2)
        self.crear_boton_accion_usuario(botones, "Limpiar", "clean", self.limpiar_formulario_usuario, 3)

        contenedor = ttk.LabelFrame(self.panel_actual, text="Usuarios registrados")
        contenedor.pack(fill="both", expand=True, padx=5, pady=10)
        tabla_frame = ttk.Frame(contenedor)
        tabla_frame.pack(fill="both", expand=True, padx=10, pady=10)

        columnas = ("id", "nombre", "rol", "usuario")
        self.tabla_usuarios = ttk.Treeview(tabla_frame, columns=columnas, show="headings")
        for columna, texto in zip(columnas, ("ID", "Nombre", "Rol", "Usuario")):
            self.tabla_usuarios.heading(columna, text=texto)
        self.tabla_usuarios.column("id", width=60)
        self.tabla_usuarios.column("nombre", width=220)
        self.tabla_usuarios.column("rol", width=140)
        self.tabla_usuarios.column("usuario", width=180)
        self.tabla_usuarios.pack(side="left", fill="both", expand=True)
        scrollbar = ttk.Scrollbar(tabla_frame, orient="vertical", command=self.tabla_usuarios.yview)
        self.tabla_usuarios.configure(yscrollcommand=scrollbar.set)
        scrollbar.pack(side="right", fill="y")

        self.tabla_usuarios.bind("<<TreeviewSelect>>", self.on_usuario_seleccionado)
        self.cargar_tabla_usuarios()
        self.entry_usuario_id.focus()

        if not getattr(self, "_atajos_usuarios_configurados", False):
            self.bind_all("<Return>", self.on_return_usuario, add="+")
            self.bind_all("<Escape>", self.on_escape_usuario, add="+")
            self._atajos_usuarios_configurados = True

    def crear_boton_accion_usuario(self, parent, texto, nombre_icono, comando, columna):
        icono = self.obtener_icono(nombre_icono)
        boton = ttk.Button(parent, text=texto, image=icono if icono is not None else "", compound="left", command=comando)
        boton.grid(row=0, column=columna, padx=5)

    def cargar_tabla_usuarios(self):
        for item in self.tabla_usuarios.get_children():
            self.tabla_usuarios.delete(item)
        for usuario in self.restaurante_servicio.listar_usuarios():
            self.tabla_usuarios.insert("", "end", iid=str(usuario.id_usuario), values=(usuario.id_usuario, usuario.nombre, usuario.rol, usuario.nombre_usuario))

    def on_usuario_seleccionado(self, event):
        seleccion = self.tabla_usuarios.selection()
        if not seleccion:
            return
        try:
            id_usuario = int(seleccion[0])
        except ValueError:
            return
        usuario = self.restaurante_servicio.buscar_usuario(id_usuario)
        if usuario is None:
            return
        self.entry_usuario_id.delete(0, tk.END)
        self.entry_usuario_id.insert(0, str(usuario.id_usuario))
        self.entry_usuario_nombre.delete(0, tk.END)
        self.entry_usuario_nombre.insert(0, usuario.nombre)
        self.combo_usuario_rol.set(usuario.rol)
        self.entry_usuario_nombre_usuario.delete(0, tk.END)
        self.entry_usuario_nombre_usuario.insert(0, usuario.nombre_usuario)
        self.entry_usuario_contrasena.delete(0, tk.END)
        self.entry_usuario_contrasena.insert(0, usuario.contrasena)

    def on_rol_seleccionado(self, event):
        # En Semana 16 solo se pueden registrar nuevos usuarios
        # como Empleado o Cliente. La cuenta Administrador existente
        # se conserva como cuenta administrativa del sistema.
        rol = self.combo_usuario_rol.get()
        if rol == "Administrador":
            self.titulo_contenido.config(text="Usuarios - Administrador")
        else:
            self.titulo_contenido.config(text="Usuarios")

    def obtener_datos_usuario_formulario(self):
        try:
            id_usuario = int(self.entry_usuario_id.get().strip())
        except ValueError:
            raise ValueError("El ID debe ser un número entero.")
        nombre = self.entry_usuario_nombre.get().strip()
        rol = self.combo_usuario_rol.get().strip()
        nombre_usuario = self.entry_usuario_nombre_usuario.get().strip()
        contrasena = self.entry_usuario_contrasena.get()
        if not nombre or not rol or not nombre_usuario or not contrasena:
            raise ValueError("Complete todos los campos del usuario.")
        return id_usuario, nombre, rol, nombre_usuario, contrasena

    def registrar_usuario(self):
        try:
            datos = self.obtener_datos_usuario_formulario()
            if datos[2] == "Administrador":
                raise ValueError("No se pueden registrar nuevos usuarios Administrador desde este formulario.")
            self.restaurante_servicio.agregar_usuario(*datos)
            messagebox.showinfo("Éxito", "Usuario registrado correctamente.", parent=self)
            self.cargar_tabla_usuarios()
            self.limpiar_formulario_usuario()
        except ValueError as error:
            messagebox.showerror("Error", str(error), parent=self)

    def actualizar_usuario(self):
        try:
            datos = self.obtener_datos_usuario_formulario()
            if datos[0] == self.usuario.id_usuario and datos[2] != "Administrador":
                raise ValueError("No puede cambiar el rol del administrador con el que está iniciada la sesión.")
            if datos[2] == "Administrador" and datos[0] != self.usuario.id_usuario:
                raise ValueError("No se puede asignar el rol Administrador a otro usuario.")
            self.restaurante_servicio.actualizar_usuario(*datos)
            messagebox.showinfo("Éxito", "Usuario actualizado correctamente.", parent=self)
            self.cargar_tabla_usuarios()
            self.limpiar_formulario_usuario()
        except ValueError as error:
            messagebox.showerror("Error", str(error), parent=self)

    def eliminar_usuario(self):
        try:
            id_usuario = int(self.entry_usuario_id.get().strip())
        except ValueError:
            messagebox.showerror("Error", "Seleccione un usuario válido.", parent=self)
            return
        if not messagebox.askyesno("Confirmar eliminación", "¿Desea eliminar el usuario seleccionado?", parent=self):
            return
        try:
            self.restaurante_servicio.eliminar_usuario(id_usuario, self.usuario.id_usuario)
            messagebox.showinfo("Éxito", "Usuario eliminado correctamente.", parent=self)
            self.cargar_tabla_usuarios()
            self.limpiar_formulario_usuario()
        except ValueError as error:
            messagebox.showerror("Error", str(error), parent=self)

    def limpiar_formulario_usuario(self):
        if not hasattr(self, "entry_usuario_id"):
            return
        for entrada in (self.entry_usuario_id, self.entry_usuario_nombre, self.entry_usuario_nombre_usuario, self.entry_usuario_contrasena):
            entrada.delete(0, tk.END)
        self.combo_usuario_rol.set("")
        if hasattr(self, "tabla_usuarios"):
            self.tabla_usuarios.selection_remove(self.tabla_usuarios.selection())
        self.titulo_contenido.config(text="Usuarios")

    def on_return_usuario(self, event):
        if hasattr(self, "entry_usuario_id") and self.titulo_contenido.cget("text").startswith("Usuarios"):
            self.registrar_usuario()
            return "break"

    def on_escape_usuario(self, event):
        if hasattr(self, "entry_usuario_id") and self.titulo_contenido.cget("text").startswith("Usuarios"):
            self.limpiar_formulario_usuario()
            return "break"

    def mostrar_productos(self):

        self.titulo_contenido.config(
            text="Productos"
        )

        self.limpiar_contenido()

        contenedor = ttk.LabelFrame(
            self.panel_actual,
            text="Gestión de productos"
        )

        contenedor.pack(
            fill="both",
            expand=True
        )

        self.crear_formulario_productos(
            contenedor
        )

        self.crear_tabla_productos(
            contenedor
        )

        self.refrescar_tabla_productos()

    # ==========================================
    # FORMULARIO
    # ==========================================

    def crear_formulario_productos(
        self,
        parent
    ):

        formulario = ttk.Frame(parent)

        formulario.pack(
            fill="x",
            padx=10,
            pady=10
        )

        ttk.Label(
            formulario,
            text="ID:"
        ).grid(
            row=0,
            column=0,
            padx=5,
            pady=5,
            sticky="e"
        )

        self.entry_id = ttk.Entry(
            formulario,
            width=12
        )

        self.entry_id.grid(
            row=0,
            column=1,
            padx=5,
            pady=5
        )

        ttk.Label(
            formulario,
            text="Nombre:"
        ).grid(
            row=0,
            column=2,
            padx=5,
            pady=5,
            sticky="e"
        )

        self.entry_nombre = ttk.Entry(
            formulario,
            width=25
        )

        self.entry_nombre.grid(
            row=0,
            column=3,
            padx=5,
            pady=5
        )

        ttk.Label(
            formulario,
            text="Precio:"
        ).grid(
            row=1,
            column=0,
            padx=5,
            pady=5,
            sticky="e"
        )

        self.entry_precio = ttk.Entry(
            formulario,
            width=12
        )

        self.entry_precio.grid(
            row=1,
            column=1,
            padx=5,
            pady=5
        )

        ttk.Label(
            formulario,
            text="Categoría:"
        ).grid(
            row=1,
            column=2,
            padx=5,
            pady=5,
            sticky="e"
        )

        self.entry_categoria = ttk.Entry(
            formulario,
            width=25
        )

        self.entry_categoria.grid(
            row=1,
            column=3,
            padx=5,
            pady=5
        )

        ttk.Label(
            formulario,
            text="Stock:"
        ).grid(
            row=2,
            column=0,
            padx=5,
            pady=5,
            sticky="e"
        )

        self.entry_stock = ttk.Entry(
            formulario,
            width=12
        )

        self.entry_stock.grid(
            row=2,
            column=1,
            padx=5,
            pady=5
        )

        botones = ttk.Frame(parent)

        botones.pack(
            fill="x",
            padx=10,
            pady=5
        )

        self.crear_boton_accion(
            botones,
            "Registrar",
            "add",
            self.agregar_producto
        )

        self.crear_boton_accion(
            botones,
            "Cargar por código",
            "search",
            self.cargar_producto
        )

        self.crear_boton_accion(
            botones,
            "Actualizar",
            "edit",
            self.actualizar_producto
        )

        self.crear_boton_accion(
            botones,
            "Eliminar",
            "delete",
            self.eliminar_producto
        )

        self.crear_boton_accion(
            botones,
            "Limpiar",
            "clean",
            self.limpiar_formulario
        )

    def crear_boton_accion(
        self,
        parent,
        texto,
        nombre_icono,
        comando
    ):

        icono = self.obtener_icono(nombre_icono)

        if icono is not None:

            boton = ttk.Button(
                parent,
                text=texto,
                image=icono,
                compound="left",
                command=comando
            )

        else:

            boton = ttk.Button(
                parent,
                text=texto,
                command=comando
            )

        boton.pack(
            side="left",
            padx=4
        )

    # ==========================================
    # TABLA
    # ==========================================

    def crear_tabla_productos(
        self,
        parent
    ):

        tabla_frame = ttk.Frame(parent)

        tabla_frame.pack(
            fill="both",
            expand=True,
            padx=10,
            pady=10
        )

        columnas = (
            "id",
            "nombre",
            "precio",
            "categoria",
            "stock"
        )

        self.tabla_productos = ttk.Treeview(
            tabla_frame,
            columns=columnas,
            show="headings"
        )

        self.tabla_productos.heading(
            "id",
            text="ID"
        )

        self.tabla_productos.heading(
            "nombre",
            text="Nombre"
        )

        self.tabla_productos.heading(
            "precio",
            text="Precio"
        )

        self.tabla_productos.heading(
            "categoria",
            text="Categoría"
        )

        self.tabla_productos.heading(
            "stock",
            text="Stock"
        )

        self.tabla_productos.column(
            "id",
            width=60
        )

        self.tabla_productos.column(
            "nombre",
            width=180
        )

        self.tabla_productos.column(
            "precio",
            width=90
        )

        self.tabla_productos.column(
            "categoria",
            width=140
        )

        self.tabla_productos.column(
            "stock",
            width=80
        )

        scrollbar = ttk.Scrollbar(
            tabla_frame,
            orient="vertical",
            command=self.tabla_productos.yview
        )

        self.tabla_productos.configure(
            yscrollcommand=scrollbar.set
        )

        self.tabla_productos.pack(
            side="left",
            fill="both",
            expand=True
        )

        scrollbar.pack(
            side="right",
            fill="y"
        )

    def refrescar_tabla_productos(self):

        for item in self.tabla_productos.get_children():

            self.tabla_productos.delete(item)

        productos = (
            self.restaurante_servicio
            .listar_productos()
        )

        for producto in productos:

            self.tabla_productos.insert(
                "",
                "end",
                values=(
                    producto.id_producto,
                    producto.nombre,
                    f"${producto.precio:.2f}",
                    producto.categoria,
                    producto.stock
                )
            )

    # ==========================================
    # CARGAR POR CÓDIGO
    # ==========================================

    def cargar_producto(self):

        try:

            id_producto = int(
                self.entry_id.get()
            )

        except ValueError:

            messagebox.showerror(
                "Error",
                "Ingrese un ID válido.",
                parent=self
            )

            return

        producto = (
            self.restaurante_servicio
            .buscar_producto(id_producto)
        )

        if producto is None:

            messagebox.showerror(
                "Error",
                "No se encontró el producto.",
                parent=self
            )

            return

        self.entry_nombre.delete(
            0,
            tk.END
        )

        self.entry_nombre.insert(
            0,
            producto.nombre
        )

        self.entry_precio.delete(
            0,
            tk.END
        )

        self.entry_precio.insert(
            0,
            producto.precio
        )

        self.entry_categoria.delete(
            0,
            tk.END
        )

        self.entry_categoria.insert(
            0,
            producto.categoria
        )

        self.entry_stock.delete(
            0,
            tk.END
        )

        self.entry_stock.insert(
            0,
            producto.stock
        )

    # ==========================================
    # REGISTRAR
    # ==========================================

    def agregar_producto(self):

        try:

            id_producto = int(
                self.entry_id.get()
            )

            nombre = (
                self.entry_nombre
                .get()
                .strip()
            )

            precio = float(
                self.entry_precio.get()
            )

            categoria = (
                self.entry_categoria
                .get()
                .strip()
            )

            stock = int(
                self.entry_stock.get()
            )

            self.restaurante_servicio.agregar_producto(
                id_producto,
                nombre,
                precio,
                categoria,
                stock
            )

            self.refrescar_tabla_productos()

            self.limpiar_formulario()

            messagebox.showinfo(
                "Éxito",
                "Producto registrado correctamente.",
                parent=self
            )

        except ValueError as error:

            messagebox.showerror(
                "Error",
                str(error),
                parent=self
            )

    # ==========================================
    # ACTUALIZAR
    # ==========================================

    def actualizar_producto(self):

        try:

            id_producto = int(
                self.entry_id.get()
            )

            nombre = (
                self.entry_nombre
                .get()
                .strip()
            )

            precio = float(
                self.entry_precio.get()
            )

            categoria = (
                self.entry_categoria
                .get()
                .strip()
            )

            stock = int(
                self.entry_stock.get()
            )

            self.restaurante_servicio.actualizar_producto(
                id_producto,
                nombre,
                precio,
                categoria,
                stock
            )

            self.refrescar_tabla_productos()

            self.limpiar_formulario()

            messagebox.showinfo(
                "Éxito",
                "Producto actualizado correctamente.",
                parent=self
            )

        except ValueError as error:

            messagebox.showerror(
                "Error",
                str(error),
                parent=self
            )

    # ==========================================
    # ELIMINAR
    # ==========================================

    def eliminar_producto(self):

        try:

            id_producto = int(
                self.entry_id.get()
            )

        except ValueError:

            messagebox.showerror(
                "Error",
                "Ingrese un ID válido.",
                parent=self
            )

            return

        producto = (
            self.restaurante_servicio
            .buscar_producto(id_producto)
        )

        if producto is None:

            messagebox.showerror(
                "Error",
                "No se encontró el producto.",
                parent=self
            )

            return

        confirmar = messagebox.askyesno(
            "Confirmar eliminación",
            f"¿Desea eliminar '{producto.nombre}'?",
            parent=self
        )

        if not confirmar:
            return

        try:

            self.restaurante_servicio.eliminar_producto(
                id_producto
            )

            self.refrescar_tabla_productos()

            self.limpiar_formulario()

            messagebox.showinfo(
                "Éxito",
                "Producto eliminado correctamente.",
                parent=self
            )

        except ValueError as error:

            messagebox.showerror(
                "Error",
                str(error),
                parent=self
            )

    # ==========================================
    # LIMPIAR
    # ==========================================

    def limpiar_formulario(self):

        self.entry_id.delete(
            0,
            tk.END
        )

        self.entry_nombre.delete(
            0,
            tk.END
        )

        self.entry_precio.delete(
            0,
            tk.END
        )

        self.entry_categoria.delete(
            0,
            tk.END
        )

        self.entry_stock.delete(
            0,
            tk.END
        )

    # ==========================================
    # VENTAS
    # ==========================================

    def mostrar_ventas(self):
        self.titulo_contenido.config(text="Ventas")
        self.limpiar_contenido()

        formulario = ttk.LabelFrame(
            self.panel_actual,
            text="Registrar venta"
        )
        formulario.pack(fill="x", padx=5, pady=5)

        ttk.Label(formulario, text="Usuario:").grid(row=0, column=0, padx=8, pady=10, sticky="w")
        self.combo_usuario_venta = ttk.Combobox(formulario, state="readonly", width=28)
        self.combo_usuario_venta.grid(row=0, column=1, padx=8, pady=10)

        ttk.Label(formulario, text="Producto:").grid(row=0, column=2, padx=8, pady=10, sticky="w")
        self.combo_producto_venta = ttk.Combobox(formulario, state="readonly", width=28)
        self.combo_producto_venta.grid(row=0, column=3, padx=8, pady=10)

        self.cargar_opciones_venta()

        icono_add = self.obtener_icono("add")
        boton_venta = ttk.Button(
            formulario,
            text="Registrar venta",
            image=icono_add if icono_add is not None else "",
            compound="left",
            command=self.registrar_venta
        )
        boton_venta.grid(row=0, column=4, padx=10, pady=10)

        contenedor = ttk.LabelFrame(
            self.panel_actual,
            text="Ventas registradas"
        )
        contenedor.pack(fill="both", expand=True, padx=5, pady=10)

        columnas = ("id", "usuario", "producto", "fecha")
        self.tabla_ventas = ttk.Treeview(
            contenedor,
            columns=columnas,
            show="headings"
        )

        for columna, texto in zip(columnas, ("ID", "Usuario", "Producto", "Fecha")):
            self.tabla_ventas.heading(columna, text=texto)

        self.tabla_ventas.column("id", width=60)
        self.tabla_ventas.column("usuario", width=180)
        self.tabla_ventas.column("producto", width=180)
        self.tabla_ventas.column("fecha", width=180)

        scrollbar = ttk.Scrollbar(
            contenedor,
            orient="vertical",
            command=self.tabla_ventas.yview
        )
        self.tabla_ventas.configure(yscrollcommand=scrollbar.set)
        self.tabla_ventas.pack(side="left", fill="both", expand=True, padx=10, pady=10)
        scrollbar.pack(side="right", fill="y", pady=10)

        self.refrescar_tabla_ventas()

    def cargar_opciones_venta(self):
        usuarios = self.restaurante_servicio.listar_usuarios()
        productos = [p for p in self.restaurante_servicio.listar_productos() if p.stock > 0]

        self.mapa_usuarios_venta = {
            f"{u.id_usuario} - {u.nombre}": u.id_usuario
            for u in usuarios
        }
        self.mapa_productos_venta = {
            f"{p.id_producto} - {p.nombre} (stock: {p.stock})": p.id_producto
            for p in productos
        }

        self.combo_usuario_venta["values"] = list(self.mapa_usuarios_venta.keys())
        self.combo_producto_venta["values"] = list(self.mapa_productos_venta.keys())

        # No seleccionar automáticamente: el usuario debe elegir
        # de forma explícita el usuario y el producto.
        self.combo_usuario_venta.set("")
        self.combo_producto_venta.set("")

    def registrar_venta(self):
        usuario_texto = self.combo_usuario_venta.get()
        producto_texto = self.combo_producto_venta.get()

        if not usuario_texto or not producto_texto:
            messagebox.showerror(
                "Error",
                "Seleccione un usuario y un producto.",
                parent=self
            )
            return

        try:
            id_usuario = self.mapa_usuarios_venta[usuario_texto]
            id_producto = self.mapa_productos_venta[producto_texto]
            self.restaurante_servicio.registrar_venta(id_usuario, id_producto)

            messagebox.showinfo(
                "Éxito",
                "Venta registrada correctamente.",
                parent=self
            )

            self.mostrar_ventas()

        except ValueError as error:
            messagebox.showerror("Error", str(error), parent=self)

    def refrescar_tabla_ventas(self):
        for item in self.tabla_ventas.get_children():
            self.tabla_ventas.delete(item)

        for venta in self.restaurante_servicio.listar_ventas():
            usuario = self.restaurante_servicio.buscar_usuario(venta.id_usuario)
            producto = self.restaurante_servicio.buscar_producto(venta.id_producto)

            nombre_usuario = usuario.nombre if usuario else "Desconocido"
            nombre_producto = producto.nombre if producto else "Producto eliminado"

            self.tabla_ventas.insert(
                "",
                "end",
                values=(
                    venta.id_venta,
                    nombre_usuario,
                    nombre_producto,
                    venta.fecha
                )
            )

    # ==========================================
    # CERRAR SESIÓN
    # ==========================================

    def confirmar_cierre(self):

        confirmar = messagebox.askyesno(
            "Cerrar sesión",
            "¿Desea cerrar la sesión?",
            parent=self
        )

        if confirmar:

            self.cerrar_sesion_callback()