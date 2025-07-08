import sqlite3
from colorama import Fore, init
init(autoreset=True)

def obtener_conexion():
    """
        Sirve para conectar con la base de datos, además sirve para crear la tabla productos si fuera necesario.
    """
    try:
        conexion = sqlite3.connect('inventario.db') # Conexión a la base de datos.
        cursor = conexion.cursor() # Creación del cursor.
        cursor.execute(""" 
                        CREATE TABLE IF NOT EXISTS productos(
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        nombre TEXT NOT NULL,
                        descripcion TEXT NOT NULL,
                        cantidad INTEGER NOT NULL,
                        precio FLOAT NOT NULL
                        )""") # Crea la tabla en caso que sea necesario.
        conexion.commit() # Guarda los cambios de la creación de tabla.
        return conexion # En caso de conexión exitosa retorna conexion.
    except sqlite3.Error as e:
        print(Fore.RED + f'Error❗ al conectar con la base de datos: {e}')
        return None # Retorna None si hay un error
    

def agregar_productos():
    '''
    Sirve para que el usuario agregue productos al sistema y sean almacenados en la base de datos ("inventario.db").
    '''
    agregando_productos = True # Bandera para cortar el ciclo "agregando productos".
    while agregando_productos:
        # Aqui le pedimos al usuario la información del producto mediante inputs
        nombre = input(Fore.YELLOW + 'Ingrese el nombre del producto: ').strip().lower()
        print(Fore.BLUE+'='*46)
        descripcion = input(Fore.YELLOW + 'Ingrese una breve descripción del producto.(max. 30 caracteres): ').strip().lower()
        print(Fore.BLUE+'='*46)
        
        while True:        
            cantidad_str = input(Fore.YELLOW + 'Ingrese el stock total del producto: ').strip()
            print(Fore.BLUE+'='*46)
            try:
                cantidad = int(cantidad_str) # Intento de convertir el string cantidad a int.
                if cantidad < 0:  # Validación de que la cantidad no sea un numero negativo.
                    print(Fore.RED + '❌ La cantidad no puede ser un número negativo. Intente de nuevo.')
                else:
                    break
            except ValueError:
                print(Fore.RED + '❌ Cantidad inválida. Por favor, ingrese un número entero.')
        
        while True: # Bucle validación de precio
            precio_str = input(Fore.YELLOW + 'Ingrese el precio del producto: ').strip()
            print(Fore.BLUE+'='*46)
            try:
                precio = float(precio_str) # Intento convertir el precio de string a float.
                if precio < 0:
                    print(Fore.RED + '❌ La cantidad no puede ser un número negativo. Intente de nuevo.')
                else:
                    break
            except ValueError:
                print(Fore.RED + '❌ Precio inválido. Por favor, ingrese un número (puede usar decimales).')
        conexion = None
        try: 
            conexion = obtener_conexion() # Intenta conectar con la base de datos mediante la función "obtener_conexion".
            if conexion:  # Verifica que la conexion haya sido exitosa.
                cursor = conexion.cursor() # Define el cursor.
                cursor.execute("""INSERT INTO productos (nombre, descripcion, cantidad, precio)
                                  VALUES (?, ?, ?, ?)""", (nombre, descripcion, cantidad, precio))
                conexion.commit()
                print(Fore.GREEN + f'Producto agregado con éxito!✅ ')
            else:
                print(Fore.RED + "No se pudo establecer conexión con la base de datos❗.")                
        except sqlite3.Error as e:
            print(Fore.RED + f'Error❗ al conectar con la base de datos: {e}')
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
        conexion = obtener_conexion()
        if conexion:  # Verifica que la conexion haya sido exitosa.
                cursor = conexion.cursor() # Define el cursor.
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
        else:
            print(Fore.RED + "No se pudo establecer conexión con la base de datos❗.")
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
        conexion = obtener_conexion()
        if conexion:
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
        else:
            print(Fore.RED + "No se pudo establecer conexión con la base de datos❗.")
    except sqlite3.Error as e:
        print(Fore.RED + f'Error al conectar con la base de datos❗: {e}')
    finally:
            if conexion:
                conexion.close()

def actualizar_por_id():
    """
    Sirve para actualizar un producto buscandolo por su ID
    """
    try:
        ver_productos()
        conexion = obtener_conexion()
        if conexion:
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
        else:
            print(Fore.RED + "No se pudo establecer conexión con la base de datos❗.")
    except sqlite3.Error as e:
        print(Fore.RED + f'Error al conectar con la base de datos❗: {e}')
    finally:
        conexion.close()

def eliminar_por_id():
    """
        Siver para eliminar un producto buscandolo por su ID.
    """
    try:
        ver_productos()
        conexion = obtener_conexion()
        if conexion:
            cursor = conexion.cursor()
            id_producto = input(Fore.YELLOW + 'Ingrese el ID del producto que desea eliminar: ').strip()
            print(Fore.BLUE+'='*46)
            while not id_producto:
                print(Fore.RED + "Id inválido")
                id_producto = input('Ingrese ID del producto que desea eliminar: ').strip()

            query = "DELETE FROM productos WHERE id = ?"
            cursor.execute(query, (id_producto,))

            if cursor.rowcount == 0: #verifica la cantidad de filas afectadas
                print(Fore.RED + f"No se encontró el producto con el id: {id_producto}.")
            else:
                conexion.commit()
                print(Fore.GREEN + f"Producto con ID: {id_producto} eliminado con éxito.")
        else:
            print(Fore.RED + "No se pudo establecer conexión con la base de datos❗.")
    except sqlite3.Error as e:
        print(Fore.RED + f'Error al conectar con la base de datos❗: {e}')
    finally:
        conexion.close()

def buscar_por_stock():
    """
    Sirve para buscar que productos tienen un stock menor al ingresado por el usuario
    """
    try:
        conexion = obtener_conexion()
        if conexion:
            cursor = conexion.cursor()
            stock_min = input(Fore.YELLOW + 'Ingrese una cantidad para filtrar los productos con stock inferior al mismo: ').strip()
            print(Fore.BLUE+'='*46)
            while not stock_min:
                print(Fore.RED + "Id inválido")
                stock_min = input(Fore.YELLOW + 'Ingrese una cantidad para filtrar los productos con stock inferior al mismo: ').strip()

            query = 'SELECT * FROM productos WHERE cantidad < ?'
            cursor.execute(query,(stock_min,))
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
                print(Fore.LIGHTCYAN_EX + '-' * (len(header)-5)) # Linea separadora superior del header de la tabla.
                print(header)                                    # Imprime el encabezado de la tabla.
                print(Fore.LIGHTCYAN_EX + '-' * (len(header)-5)) # Linea separadora inferior del header de la tabla.
                
                for producto in productos:
                    precio_formateado = f"{producto[4]:.2f}" # Foramtea el precio a 2 decimales.
                    nombre_recortado = (str(producto[1])[:ancho_nombre]).ljust(ancho_nombre) # Recorta el nombre al ancho max proporcionado.
                    descripcion_recortada = (str(producto[2])[:ancho_descripcion]).ljust(ancho_descripcion) # Recrota la descripción al max proporcionado.
                    print(
                        f"| {producto[0]:^{ancho_id}} "            # ID alineado al centro
                        f"| {nombre_recortado.title()} "           # Nombre alineado a la izquierda
                        f"| {descripcion_recortada.title()} "      # Descripción alineada a la izquierda
                        f"| {producto[3]:^{ancho_cantidad}} "      # Cantidad alineada al centro
                        f"| {precio_formateado:>{ancho_precio}} |" # Precio alineado a la derecha
                    )
                print(Fore.LIGHTCYAN_EX + '-' * (len(header) - 5)) # Línea final de la tabla.

        else:
            print(Fore.RED + "No se pudo establecer conexión con la base de datos❗.")
    except sqlite3.Error as e:
        print(Fore.RED + f'Error al conectar con la base de datos❗: {e}')
    finally:
        conexion.close()