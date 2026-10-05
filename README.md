# Restaurante App - Semana 16

## Tema

**Semana 16: manejo de eventos con Tkinter aplicado a la gestión de usuarios en Restaurante App.**

## Objetivo

Evolucionar el proyecto de la Semana 15 **sin reconstruirlo desde cero**. La aplicación conserva el inicio de sesión, la arquitectura modular, la persistencia JSON, la gestión de productos, el registro de ventas, el menú lateral y la identidad visual.

En esta semana la sección **Usuarios** se convierte en una gestión sencilla e interactiva para evidenciar el flujo entre una acción del usuario, un evento de Tkinter, `bind()`, un callback con `event`, `RestauranteServicio`, la persistencia y la respuesta visual.

## Continuidad desde Semana 15

Se conservan los componentes y recursos visuales desarrollados previamente. La sección **Ventas** continúa como ejemplo del uso de `command=` y callbacks. La sección **Usuarios** se convierte en el ejemplo principal del manejo de eventos.

## Nueva funcionalidad de Semana 16

La gestión de usuarios permite:

- Registrar usuarios.
- Consultar usuarios.
- Seleccionar un usuario desde un `ttk.Treeview`.
- Cargar automáticamente los datos seleccionados en el formulario.
- Actualizar usuarios.
- Eliminar usuarios con confirmación.
- Limpiar o cancelar la selección.
- Trabajar con roles simples.

### Roles

El modelo contempla:

- `Administrador`
- `Empleado`
- `Cliente`

La cuenta `Administrador` existente se conserva como cuenta administrativa del sistema. Desde el formulario de gestión solo se pueden registrar nuevos usuarios como **Empleado** o **Cliente**.

Flujo educativo:

```text
Interacción del usuario
        ↓
evento Tkinter
        ↓
bind()
        ↓
callback(event)
        ↓
RestauranteServicio
        ↓
usuarios.json
        ↓
interfaz actualizada
```

## Eventos implementados

La sección Usuarios evidencia la diferencia entre botones con `command=` y eventos mediante `bind()`.

### Botones con `command=`

- Registrar
- Actualizar
- Eliminar
- Limpiar

### Eventos con `bind()`

- `<<TreeviewSelect>>`: al seleccionar una fila, carga el usuario en el formulario.
- `<Return>`: registra un usuario desde el formulario.
- `<Escape>`: limpia el formulario y cancela la selección.
- `<<ComboboxSelected>>`: detecta el cambio de rol.

Flujo principal del Treeview:

```text
Treeview
   ↓
identificador
   ↓
RestauranteServicio.buscar_usuario()
   ↓
objeto Usuario
   ↓
formulario
```

## Estructura del proyecto

```text
restaurante_app/
├── assets/
│   ├── icons/
│   │   ├── home.png
│   │   ├── users.png
│   │   ├── products.png
│   │   ├── logout.png
│   │   ├── add.png
│   │   ├── edit.png
│   │   ├── delete.png
│   │   ├── search.png
│   │   └── clean.png
│   └── logo/
│       ├── logo.png
│       └── icono.png
├── datos/
│   ├── productos.json
│   ├── usuarios.json
│   └── ventas.json
├── modelos/
│   ├── usuario.py
│   ├── producto.py
│   └── venta.py
├── servicios/
│   ├── archivo_servicio.py
│   └── restaurante_servicio.py
├── ui/
│   ├── login_view.py
│   └── main_view.py
└── main.py
```

## Capas

**modelos/**: define `Usuario`, `Producto` y `Venta`. `Usuario` incluye el atributo `rol` y validaciones básicas.

**servicios/**: contiene las operaciones de consulta, registro, actualización, eliminación y persistencia. `RestauranteServicio` administra el CRUD de usuarios y mantiene las operaciones de productos y ventas.

**datos/**: conserva la información persistente en archivos JSON.

**ui/**: contiene las vistas creadas con Tkinter y coordina las interacciones mediante `command=` y `bind()`.

**assets/**: contiene los iconos PNG y el logo utilizados por la interfaz.

## Pantallas principales

- **LoginView**: inicio de sesión.
- **Inicio**: resumen del sistema.
- **Usuarios**: gestión de usuarios disponible para Administrador.
- **Productos**: gestión de productos.
- **Ventas**: selección de usuario y producto para registrar una venta sencilla.

## Componentes Tkinter utilizados

- `Label`: textos y títulos.
- `Entry`: campos de entrada.
- `ttk.Combobox`: selección de roles y selección de usuario/producto en ventas.
- `ttk.Button`: navegación y acciones con `command=`.
- `ttk.Treeview`: tablas de usuarios, productos y ventas.
- `ttk.Scrollbar`: desplazamiento de tablas.
- `messagebox`: mensajes, errores y confirmaciones.

## Persistencia

Los usuarios, productos y ventas se cargan desde JSON al iniciar la aplicación.

```text
restaurante_app/datos/usuarios.json
restaurante_app/datos/productos.json
restaurante_app/datos/ventas.json
```

Al registrar, actualizar o eliminar usuarios, `RestauranteServicio` actualiza la colección en memoria y solicita a `ArchivoServicio` que escriba `usuarios.json`.

## Control de acceso

La aplicación utiliza el objeto `usuario_actual` recibido por `MainView`.

- **Administrador**: puede ver y utilizar la sección Usuarios.
- **Empleado** y **Cliente**: no ven la opción Usuarios en el menú lateral.

No se implementa un sistema avanzado de permisos; el objetivo es mantener el ejemplo claro y acorde con la Semana 16.

## Validaciones principales

La gestión de usuarios contempla:

- campos obligatorios;
- rol válido;
- identificador duplicado;
- nombre de usuario duplicado;
- usuario inexistente al actualizar o eliminar;
- ausencia de selección;
- confirmación antes de eliminar;
- protección del usuario actualmente autenticado;
- no registrar nuevos Administradores desde el formulario;
- no cambiar el rol del Administrador actualmente autenticado.

## Cómo ejecutar

Desde la carpeta `restaurante_app`:

```bash
py main.py
```

Si `python` está disponible:

```bash
python main.py
```

## Credenciales de demostración

**Administrador**

- Usuario: `richi`
- Contraseña: `6666`

**Cliente**

- Usuario: `maria`
- Contraseña: `1234`

## Cómo probar la gestión de usuarios

1. Iniciar la aplicación.
2. Acceder con `richi / 6666`.
3. Verificar que aparece la opción **Usuarios**.
4. Entrar a **Usuarios**.
5. Registrar un usuario con rol **Cliente**.
6. Registrar un usuario con rol **Empleado**.
7. Seleccionar una fila del `Treeview` y verificar que sus datos se cargan automáticamente.
8. Modificar los datos y pulsar **Actualizar**.
9. Seleccionar un usuario y pulsar **Eliminar**; confirmar la eliminación.
10. Verificar que la cuenta Administrador actualmente autenticada no pueda eliminarse.
11. Usar `Escape` para limpiar el formulario y quitar la selección.
12. Usar `Enter` para registrar desde el formulario.
13. Cambiar el rol en el `Combobox` y comprobar `<<ComboboxSelected>>`.
14. Reiniciar la aplicación y comprobar que los cambios permanecen en `usuarios.json`.
15. Comprobar que Productos y Ventas de la Semana 15 continúen funcionando.
