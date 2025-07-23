# 📦 Mi Primer Inventario con Python 🚀

Este es un pequeño proyecto que hice con Python para aprender a manejar un inventario. En el podés llevar registro de tus productos, ver qué tenés, cambiarlos o borrarlos. ¡Y todo desde la consola!

---

## ✨ ¿Qué hace esta app?

Esta aplicación es un **CRUD**. Vas a poder:

* ✅ **Agregar productos nuevos:** 
* *️⃣ **Ver todos los productos:** 
* 🔍 **Buscar productos por ID:**
* ✏️ **Actualizar productos por ID:** 
* ❌ **Eliminar productos por ID:** 
* 📉 **Buscar productos por stock bajo:** 

Toda la info se guarda en un archivo de base de datos (`inventario.db`) usando **SQLite**.

---
## 🧱 Estructura del proyecto

```
CRUD_TT
├── main.py             # 👉 Desde acá arrancás el programa. Muestra el menú y maneja lo que elegís.
├── modulos/
│   ├── menu.py         # 👉 Acá están las funciones para mostrar los menús bonitos en la consola.
│   └── productos.py    # 👉 Este tiene toda la lógica de la base de datos (guardar, buscar, etc.).
└── inventario.db       # 👉 Este archivo se crea solo cuando usás la app por primera vez y guarda tus productos.

```

---

## 🛠️ Lo que vas a necesitar

* **Python 3.8:**
* **`colorama`:** Una librería de Python para que los mensajes en la consola tengan colores.

### instalación  `colorama`!

Abrí tu terminal (la consola de comandos) y poné esto:

```bash
pip install colorama
```
---

## ▶️ Cómo usar la aplicación

Desde la terminal:

```bash
python main.py
```

Seguí las opciones del menú para:

1. Agregar productos.
2. Ver todos los productos.
3. Busqueda de producto por ID.
4. Actualizar productos por ID.
5. Eliminar producto por ID.
6. Buscar productos por stock.
0. Salir del programa.

---

## 🧑‍💻 Autor

**Gabriel Calleja**

---

## 🪪 Licencia

Este proyecto está bajo la Licencia MIT.
