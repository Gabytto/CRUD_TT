import sqlite3
from colorama import Fore, init, Style
init(autoreset=True)

try:
    conexion = sqlite3.connect('inventario.db') # Creación de la conexión a la base de datos.
    print(Fore.CYAN + 'Conexión establecida exitosamente.') 
    cursor = conexion.cursor() # Creación del cursor.
    cursor.execute(""" 
                    CREATE TABLE IF NOT EXISTS productos(
                   id INTEGER PRIMARY KEY AUTOINCREMENT,
                   nombre TEXT NOT NULL,
                   descripcion TEXT NOT NULL,
                   cantidad INTEGER NOT NULL,
                   precio FLOAT NOT NULL
                   )""") # Crea la tabla en caso que sea necesario.
    
except sqlite3.Error as e:
    print(Fore.RED + f'Error al conectar con la base de datos: {e}')

finally:
    if conexion:
        conexion.close()
        print(Fore.CYAN + 'Conexión cerrada.') # Cierre de la conexión.

def agregar_productos():
    '''
    Sirve para agregar productos al sistema.
    '''
    agregando_productos = True
    while agregando_productos:

        nombre = input(Fore.YELLOW + 'Ingrese el nombre del producto: ').strip().lower()
        print(Fore.BLUE+'='*46)
        descripcion = input(Fore.YELLOW + 'Ingrese una breve descripción del producto.(max. 30 caracteres): ').strip().lower()
        print(Fore.BLUE+'='*46)
        cantidad = input(Fore.YELLOW + 'Ingrese el stock total del producto: ').strip()
        print(Fore.BLUE+'='*46)
        precio = input(Fore.YELLOW + 'Ingrese el precio del producto: ').strip()
        print(Fore.BLUE+'='*46)

        try: 
            conexion = sqlite3.connect('inventario.db')
            cursor = conexion.cursor()
            cursor.execute("""
                           INSERT INTO productos (nombre, descripcion, cantidad, precio)
                           VALUES (?, ?, ?, ?)""", (nombre, descripcion, cantidad, precio))
            conexion.commit()
            print(Fore.GREEN + f'Producto agregado con éxito! ')
        except sqlite3.Error as e:
            print(Fore.RED + f'Error al conectar con la base de datos: {e}')
        finally:
            if conexion:
                conexion.close()
                
        while True:
            continuar_agregando = input(Fore.YELLOW + 'Desea continuar agregando productos? (s/n): ').strip().lower()
            if continuar_agregando == 's':
                print(Fore.BLUE+'='*46)
                continue
            elif continuar_agregando == 'n':
                print(Fore.BLUE+'='*46)
                print('Volviendo al menú principal...')
                agregando_productos = False
                break
            else:
                print(Fore.BLUE+'='*46)
                print(Fore.RED + 'La opción ingresada no es válida')
                print(Fore.BLUE+'='*46)
                continue
            
def ver_productos():
    '''
    Sirve para consultar el listado de productos completo y armar una tabla que los contenga.
    '''
    try: 
        conexion = sqlite3.connect('inventario.db')
        cursor = conexion.cursor()
        cursor.execute('SELECT * FROM productos')
        productos = cursor.fetchall()
        if not productos:
            print(Fore.RED + 'No hay productos almacenados.')
        else:
            ancho_id = 10
            ancho_nombre = 20 
            ancho_descripcion = 30 
            ancho_cantidad = 12
            ancho_precio = 12

            header = (
                Fore.LIGHTCYAN_EX + 
                f"| {'ID':^{ancho_id}} "
                f"| {'NOMBRE':^{ancho_nombre}} "
                f"| {'DESCRIPCION':^{ancho_descripcion}} "
                f"| {'CANTIDAD':^{ancho_cantidad}} "
                f"| {'PRECIO':^{ancho_precio}} |"
            ) 
            print(Fore.LIGHTCYAN_EX + '-' * (len(header)-5)) # Ajusta la línea separadora al ancho total
            print(header)
            print(Fore.LIGHTCYAN_EX + '-' * (len(header)-5))
            
            for producto in productos:
                precio_formateado = f"{producto[4]:.2f}" # Foramtea el precio a 2 decimales
                nombre_recortado = (str(producto[1])[:ancho_nombre]).ljust(ancho_nombre) # Recorta el nombre al ancho max proporcionado
                descripcion_recortada = (str(producto[2])[:ancho_descripcion]).ljust(ancho_descripcion) # Recrota la descripción al max proporcionado
                print(
                    f"| {producto[0]:^{ancho_id}} " # ID alineado al centro
                    f"| {nombre_recortado.title()} " # Nombre alineado a la izquierda
                    f"| {descripcion_recortada.title()} " # Descripción alineada a la izquierda
                    f"| {producto[3]:^{ancho_cantidad}} " # Cantidad alineada al centro
                    f"| {precio_formateado:>{ancho_precio}} |" # Precio alineado a la derecha
                )
            print(Fore.LIGHTCYAN_EX + '-' * (len(header) - 5)) # Línea final de la tabla

    except sqlite3.Error as e:
        print(Fore.RED + f'Error al conectar con la base de datos: {e}')
    finally:
            if conexion:
                conexion.close()
    
def busqueda_por_id():
    """
    Sirve para buscar productos por su ID.
    """
    try: 
        id = input(Fore.YELLOW + 'Ingrese el ID del producto que desea buscar.')
        conexion = sqlite3.connect('inventario.db')
        cursor = conexion.cursor()
        cursor.execute('SELECT * FROM productos WHERE id = ?', (id,))
        producto = cursor.fetchone()
        if not producto:
            print(Fore.RED + 'No hay productos almacenados con ese ID.')
        else:
            ancho_id = 10
            ancho_nombre = 20 
            ancho_descripcion = 30 
            ancho_cantidad = 12
            ancho_precio = 12

            header = (
                Fore.LIGHTCYAN_EX + 
                f"| {'ID':^{ancho_id}} "
                f"| {'NOMBRE':^{ancho_nombre}} "
                f"| {'DESCRIPCION':^{ancho_descripcion}} "
                f"| {'CANTIDAD':^{ancho_cantidad}} "
                f"| {'PRECIO':^{ancho_precio}} |"
            ) 
            print(Fore.LIGHTCYAN_EX + '-' * (len(header)-5))# Ajusta la línea separadora al ancho total
            print(header)
            print(Fore.LIGHTCYAN_EX + '-' * (len(header)-5)) 
            precio_formateado = f"{producto[4]:.2f}" # Foramtea el precio a 2 decimales
            nombre_recortado = (str(producto[1])[:ancho_nombre]).ljust(ancho_nombre) # Recorta el nombre al ancho max proporcionado
            descripcion_recortada = (str(producto[2])[:ancho_descripcion]).ljust(ancho_descripcion) # Recrota la descripción al max proporcionado
            print(
                f"| {producto[0]:^{ancho_id}} " # ID alineado al centro
                f"| {nombre_recortado} " # Nombre alineado a la izquierda
                f"| {descripcion_recortada} " # Descripción alineada a la izquierda
                f"| {producto[3]:^{ancho_cantidad}} " # Cantidad alineada al centro
                f"| {precio_formateado:>{ancho_precio}} |" # Precio alineado a la derecha
            )
            print(Fore.LIGHTCYAN_EX + '-' * (len(header) - 5))
    except sqlite3.Error as e:
        print(Fore.RED + f'Error al conectar con la base de datos: {e}')
    finally:
            if conexion:
                conexion.close()

def actualizar_por_id():
    """
    Sirve para actualizar un producto buscandolo por su ID
    """
    try:
        ver_productos()
        conexion = sqlite3.connect('inventario.db')
        cursor = conexion.cursor()
        id_producto = input(Fore.YELLOW + 'Ingrese el ID del producto que desea modificar: ').strip()
        print(Fore.BLUE+'='*46)
        while not id_producto:
            print(Fore.RED + "Id inválido")
            id_producto = input('Ingrese ID del producto que desea modificar').strip()
        nuevo_nombre = input(Fore.YELLOW + 'Ingrese el nuevo nombre para el producto seleccionado: ').strip().lower()
        print(Fore.BLUE+'='*46)
        nueva_descripcion = input(Fore.YELLOW + 'Ingrese la nueva descripción para el producto seleccionado: ').strip().lower()
        print(Fore.BLUE+'='*46)
        nueva_cantidad = input(Fore.YELLOW + 'Ingrese la nueva cantidad para el producto seleccionado: ').strip()
        print(Fore.BLUE+'='*46)
        nuevo_precio = input(Fore.YELLOW + 'Ingrese el nuevo precio para el producto seleccionado: ').strip()
        print(Fore.BLUE+'='*46)

        query = """
                    UPDATE productos
                    SET nombre = ?, descripcion = ?, cantidad = ?, precio = ?
                    WHERE id = ?
                """
        cursor.execute(query, (nuevo_nombre, nueva_descripcion, nueva_cantidad, nuevo_precio, id_producto))
        if cursor.rowcount == 0: #verifica la cantidad de filas afectadas
            print(Fore.RED + f"No se encontró el producto con el id: {id_producto}")
        else:
            conexion.commit()
            print(Fore.GREEN + f"Producto con ID: {id_producto} modificado con éxito.")

    except sqlite3.Error as e:
        print(Fore.RED+f"Error al modificar el producto {e}")

    finally:
        conexion.close()
        print('Conexión finalizada.')

