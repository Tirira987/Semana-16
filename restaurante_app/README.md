# Restaurante App — Semana 15

Proyecto académico de **Programación Orientada a Objetos en Python con Tkinter**.

## Objetivo de la Semana 15

La Semana 15 evoluciona el sistema del restaurante construido previamente incorporando
la **gestión de ventas**, manteniendo la arquitectura modular y la interfaz desarrollada
en las semanas anteriores.

Se conserva la estructura de modelos, servicios, interfaz gráfica, persistencia en
archivos JSON y recursos visuales de la carpeta `assets/`.

## Funcionalidades

- Inicio de sesión mediante `LoginView`.
- Navegación entre Inicio, Productos, Usuarios y Ventas.
- Consulta de usuarios.
- CRUD de productos: registrar, cargar, actualizar, eliminar y limpiar.
- Registro y consulta de ventas.
- Selección explícita de usuario y producto para registrar una venta.
- Validación de stock antes de registrar una venta.
- Descuento automático de una unidad de stock después de una venta.
- Persistencia de productos y ventas en archivos JSON.
- Uso de `command=` para ejecutar las acciones de los botones.
- Uso de callbacks para separar la interacción de la lógica del servicio.
- Integración de logo, icono y recursos gráficos mediante la carpeta `assets/`.

## Corrección aplicada en la sección Ventas

La sección de ventas no selecciona automáticamente el primer usuario ni el primer
producto. Los `Combobox` se mantienen vacíos al abrir la sección y el usuario debe
seleccionar explícitamente ambas opciones antes de registrar la venta.

Esto evita registrar accidentalmente una venta con la primera opción de cada lista.

## Interfaz y experiencia de usuario

Se mantiene la organización de la interfaz existente:

- Menú lateral con iconos.
- Logo del restaurante.
- Contenedores mediante `Frame` y `LabelFrame`.
- Formularios organizados con `grid`.
- Botones de acciones con iconos de `assets/icons/`.
- Tablas `Treeview` con encabezados y barras de desplazamiento.
- Sección de ventas integrada visualmente con el resto del sistema.
- Estilos de botones, tablas y encabezados para mejorar la legibilidad.

## Carpeta de recursos

```text
assets/
├── logo/
│   ├── logo.png
│   └── icono.png
└── icons/
    ├── home.png
    ├── users.png
    ├── products.png
    ├── add.png
    ├── edit.png
    ├── delete.png
    ├── search.png
    ├── clean.png
    └── logout.png
```

El programa carga los recursos mediante rutas basadas en la ubicación de los archivos
Python, evitando depender de la carpeta desde la que se ejecute el comando.

## Arquitectura

```text
restaurante_app/
├── assets/
│   ├── icons/
│   └── logo/
├── datos/
│   ├── productos.json
│   ├── usuarios.json
│   └── ventas.json
├── modelos/
│   ├── producto.py
│   ├── usuario.py
│   └── venta.py
├── servicios/
│   ├── archivo_servicio.py
│   └── restaurante_servicio.py
├── ui/
│   ├── login_view.py
│   └── main_view.py
└── main.py
```

### Responsabilidades

- **modelos:** representan Producto, Usuario y Venta.
- **servicios:** contienen la lógica de negocio y la persistencia.
- **ui:** contiene las vistas Tkinter y las acciones de interacción.
- **datos:** almacena la información persistente en JSON.
- **assets:** contiene los recursos visuales del sistema.
- **main.py:** inicia la aplicación y conecta las vistas con los servicios.

## Persistencia de ventas

Las ventas se almacenan en:

```text
datos/ventas.json
```

Cada venta conserva su identificador, usuario, producto y fecha.

## Ejecución

Desde la carpeta `restaurante_app`:

```bash
python main.py
```

## Credenciales de prueba

- Usuario: `richi`
- Contraseña: `6666`

También está disponible el usuario:

- Usuario: `maria`
- Contraseña: `1234`

## Pruebas realizadas/recomendadas

1. Iniciar la aplicación y comprobar que aparece el login.
2. Ingresar con las credenciales de prueba.
3. Comprobar la navegación del menú lateral.
4. Abrir Productos y comprobar sus botones e iconos.
5. Abrir Ventas y comprobar que los dos `Combobox` empiezan vacíos.
6. Seleccionar manualmente un usuario y un producto.
7. Registrar una venta.
8. Comprobar que la venta aparece en la tabla.
9. Comprobar que el stock del producto disminuye.
10. Cerrar y volver a ejecutar la aplicación para comprobar la persistencia.

## Tecnologías

- Python 3
- Tkinter / ttk
- JSON
- Programación Orientada a Objetos
- Arquitectura modular


## Semana 16
Gestión de usuarios con roles, CRUD, TreeviewSelect, bind(), Return, Escape y ComboboxSelected, manteniendo Productos, Ventas y assets de Semana 15.
