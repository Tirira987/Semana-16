# Restaurante App - Semana 16

## Datos del estudiante

**Nombre:** Richard Arturo Tirira Díaz  
**Carrera:** Tecnologías de la Información  
**Asignatura:** Programación Orientada a Objetos  
**Semana:** 16

---

## Descripción

La presente actividad corresponde a la Semana 16 de la asignatura Programación Orientada a Objetos y tiene como objetivo aplicar el manejo de eventos en Tkinter dentro del proyecto `restaurante_app`.

En esta semana se continúa con la aplicación desarrollada anteriormente, conservando la arquitectura modular, la persistencia mediante archivos JSON, la organización visual y las funcionalidades implementadas.

La principal evolución corresponde a la gestión de usuarios, permitiendo registrar, consultar, actualizar y eliminar usuarios mediante un formulario y un `Treeview`.

Además, se incorporan eventos de Tkinter mediante `bind()`, callbacks y eventos virtuales, utilizando `<<TreeviewSelect>>`, `<Return>`, `<Escape>` y `<<ComboboxSelected>>`.

---

## Funcionalidades

- Inicio de sesión.
- Navegación de la aplicación.
- Gestión de productos.
- Registro de ventas.
- Gestión de usuarios.
- Registro de usuarios.
- Consulta de usuarios.
- Actualización de usuarios.
- Eliminación de usuarios.
- Manejo de roles:
  - Administrador
  - Empleado
  - Cliente
- Persistencia de información mediante archivos JSON.
- Selección de usuarios mediante `Treeview`.
- Uso de `bind()` para manejar eventos.
- Uso de callbacks para responder a los eventos.
- Uso de `command=` en los botones principales.
- Evento `<<TreeviewSelect>>` para cargar los datos del usuario seleccionado.
- Evento `<Return>` para registrar un usuario.
- Evento `<Escape>` para limpiar el formulario y la selección.
- Evento `<<ComboboxSelected>>` para responder al cambio de rol.
- Confirmación antes de eliminar usuarios.
- Protección de la cuenta del administrador actualmente autenticado.

---

## Estructura del proyecto

```text
Repositorio GitHub
├── restaurante_app/
│   ├── datos/
│   │   ├── productos.json
│   │   ├── usuarios.json
│   │   └── ventas.json
│   ├── modelos/
│   │   ├── __init__.py
│   │   ├── producto.py
│   │   ├── usuario.py
│   │   └── venta.py
│   ├── servicios/
│   │   ├── __init__.py
│   │   ├── archivo_servicio.py
│   │   └── restaurante_servicio.py
│   ├── ui/
│   │   ├── __init__.py
│   │   ├── login_view.py
│   │   └── main_view.py
│   ├── assets/
│   └── main.py
└── README.md
```
