import sqlite3
from colorama import Fore, init
init(autoreset=True)
from modulos.menu import menu_actualizar_producto

def obtener_conexion():
    """
        Permite conectar con la base de datos y, si es necesario, crear la tabla de productos.
    """
    conexion = None # Inicializa conexion a None
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
        print(Fore.RED + f'Error❗ al conectar con la base de datos: {e}. ❌')
        return None # Retorna None si hay un error
    finally:
        if conexion:
            pass

def agregar_productos():
    '''
        Permite al usuario agregar productos al sistema, los cuales son almacenados en la base de datos ("inventario.db").
    '''
    agregando_productos = True # Bandera para cortar el ciclo "agregando productos".
    while agregando_productos:
        #Aquí le pedimos al usuario la información del producto mediante entradas y validamos los datos.
        while True:
            nombre = input(Fore.YELLOW + 'Ingrese el nombre del producto: ').strip().lower()
            if not nombre:
                print(Fore.RED + 'El nombre del producto no puede estar vacío. Inténtelo de nuevo. ❌')
            else:
                break
        print(Fore.BLUE+'='*46)
        while True:
            descripcion = input(Fore.YELLOW + 'Ingrese una breve descripción del producto (máx. 30 caracteres): ').strip().lower()
            if not descripcion:
                print(Fore.RED + 'La descripción del producto no puede estar vacía. Inténtelo de nuevo. ❌')
            elif len(descripcion) > 30: # Asegura que la descripción no exceda el límite.
                print(Fore.RED + 'La descripción es demasiado larga. Máximo 30 caracteres. Inténtelo de nuevo. ❌')
            else:
                break
        print(Fore.BLUE+'='*46)
        
        while True:        
            cantidad_str = input(Fore.YELLOW + 'Ingrese el stock total del producto: ').strip()
            print(Fore.BLUE+'='*46)
            try:
                cantidad = int(cantidad_str) # Intenta convertir el string "cantidad" a tipo int.
                if cantidad < 0:  # Validación de que la cantidad no sea un número negativo.
                    print(Fore.RED + 'La cantidad no puede ser un número negativo. Inténtelo de nuevo. ❌')
                else:
                    break
            except ValueError:
                print(Fore.RED + 'Cantidad inválida. Por favor, ingrese un número entero. ❌')
        
        while True: # Bucle validación de precio
            precio_str = input(Fore.YELLOW + 'Ingrese el precio del producto: ').strip()
            print(Fore.BLUE+'='*46)
            try:
                precio = float(precio_str) # Intenta convertir el precio de string a float.
                if precio < 0:
                    print(Fore.RED + 'El precio no puede ser un número negativo. Inténtelo de nuevo. ❌')
                else:
                    break
            except ValueError:
                print(Fore.RED + 'Precio inválido❗ Por favor, ingrese un número (puede usar decimales).')
        conexion = None
        try: 
            conexion = obtener_conexion() # Intenta conectar con la base de datos mediante la función "obtener_conexion()".
            if conexion:  # Verifica que la conexión haya sido exitosa.
                cursor = conexion.cursor() # Define el cursor.
                cursor.execute("""INSERT INTO productos (nombre, descripcion, cantidad, precio)
                                  VALUES (?, ?, ?, ?)""", (nombre, descripcion, cantidad, precio))
                conexion.commit()
                print(Fore.GREEN + f'Producto agregado con éxito. ✅')
            else:
                print(Fore.RED + 'No se pudo establecer conexión con la base de datos. ❌')                
        except sqlite3.Error as e:
            print(Fore.RED + f'Error❗ al conectar con la base de datos: {e}. ❌')
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
                print(Fore.RED + 'La opción ingresada no es válida. Inténtelo de nuevo. ❌')
                print(Fore.BLUE+'='*46)
                continue
            
def ver_productos():
    '''
        Permite consultar el listado completo de productos y mostrarlos en una tabla.
    '''
    try: 
        conexion = obtener_conexion()
        if conexion:  # Verifica que la conexión haya sido exitosa.
                cursor = conexion.cursor() # Define el cursor.
                cursor.execute('SELECT * FROM productos')
                productos = cursor.fetchall()
                if not productos:
                    print(Fore.RED + 'No hay productos almacenados. ❌')
                    return False
                else:                           # Define el ancho de las columnas.
                    ancho_id = 10
                    ancho_nombre = 20 
                    ancho_descripcion = 30 
                    ancho_cantidad = 12
                    ancho_precio = 12
                                                # Estructura del encabezado de la tabla.
                    header = (
                        Fore.LIGHTCYAN_EX + 
                        f'| {'ID':^{ancho_id}} '
                        f'| {'NOMBRE':^{ancho_nombre}} '
                        f'| {'DESCRIPCION':^{ancho_descripcion}} '
                        f'| {'CANTIDAD':^{ancho_cantidad}} '
                        f'| {'PRECIO':^{ancho_precio}} |'
                        ) 
                    print(Fore.LIGHTCYAN_EX + '-' * (len(header)-5)) # Ajusta la línea separadora al ancho total.
                    print(header)
                    print(Fore.LIGHTCYAN_EX + '-' * (len(header)-5))
                    
                    for producto in productos:
                        precio_formateado = f'{producto[4]:.2f}' # Formatea el precio a 2 decimales.
                        nombre_recortado = (str(producto[1])[:ancho_nombre]).ljust(ancho_nombre) # Recorta el nombre al ancho máximo proporcionado y lo alinea a la izquierda.
                        descripcion_recortada = (str(producto[2])[:ancho_descripcion]).ljust(ancho_descripcion) # Recorta la descripción al máximo proporcionado.
                        print(
                            f'| {producto[0]:^{ancho_id}} '             # ID alineado al centro
                            f'| {nombre_recortado.title()} '            # Nombre alineado a la izquierda
                            f'| {descripcion_recortada.title()} '       # Descripción alineada a la izquierda
                            f'| {producto[3]:^{ancho_cantidad}} '       # Cantidad alineada al centro
                            f'| {precio_formateado:>{ancho_precio}} |'  # Precio alineado a la derecha
                        )
                    print(Fore.LIGHTCYAN_EX + '-' * (len(header) - 5)) # Línea final de la tabla
                    return True
        else:
            print(Fore.RED + 'No se pudo establecer conexión con la base de datos. ❌')
            return False
    except sqlite3.Error as e:
        print(Fore.RED + f'Error❗ al conectar con la base de datos: {e}. ❌')
        return False    
    finally:
            if conexion:
                conexion.close()
    
def busqueda_por_id():
    """
        Permite buscar productos por su ID.
    """
    try: 
        while True:
            id_str = input(Fore.YELLOW + 'Ingrese el ID del producto que desea buscar: ').strip()
            print(Fore.BLUE + '=' * 46) 
            if not id_str:
                print(Fore.RED + 'El ID no puede estar vacío. Inténtelo de nuevo. ❌')
                continue
            try:
                id_producto = int(id_str)
                break
            except ValueError:
                print(Fore.RED + 'ID inválido. Por favor, ingrese un número entero. ❌')
        conexion = obtener_conexion()
        if conexion:
            cursor = conexion.cursor()
            cursor.execute('SELECT * FROM productos WHERE id = ?', (id_producto,))
            producto = cursor.fetchone()
            if not producto:
                print(Fore.RED + 'No hay productos almacenados con ese ID. ❌')
            else:
                ancho_id = 10
                ancho_nombre = 20 
                ancho_descripcion = 30 
                ancho_cantidad = 12
                ancho_precio = 12

                header = (
                        Fore.LIGHTCYAN_EX + 
                        f'| {'ID':^{ancho_id}} '
                        f'| {'NOMBRE':^{ancho_nombre}} '
                        f'| {'DESCRIPCION':^{ancho_descripcion}} '
                        f'| {'CANTIDAD':^{ancho_cantidad}} '
                        f'| {'PRECIO':^{ancho_precio}} |'
                    ) 
                print(Fore.LIGHTCYAN_EX + '-' * (len(header)-5))# Ajusta la línea separadora al ancho total.
                print(header)
                print(Fore.LIGHTCYAN_EX + '-' * (len(header)-5)) 
                precio_formateado = f'{producto[4]:.2f}' # Formatea el precio a 2 decimales.
                nombre_recortado = (str(producto[1])[:ancho_nombre]).ljust(ancho_nombre) # Recorta el nombre al ancho máximo proporcionado.
                descripcion_recortada = (str(producto[2])[:ancho_descripcion]).ljust(ancho_descripcion) # Recorta la descripción al máximo proporcionado.
                print(
                    f'| {producto[0]:^{ancho_id}} '             # ID alineado al centro.
                    f'| {nombre_recortado.title()} '            # Nombre alineado a la izquierda.
                    f'| {descripcion_recortada.title()} '       # Descripción alineada a la izquierda.
                    f'| {producto[3]:^{ancho_cantidad}} '       # Cantidad alineada al centro.
                    f'| {precio_formateado:>{ancho_precio}} |'  # Precio alineado a la derecha.
                )
                print(Fore.LIGHTCYAN_EX + '-' * (len(header) - 5))
        else:
            print(Fore.RED + 'No se pudo establecer conexión con la base de datos. ❌')
    except sqlite3.Error as e:
        print(Fore.RED + f'Error❗ al conectar con la base de datos: {e}. ❌')
    finally:
            if conexion:
                conexion.close()

def actualizar_por_id():
    """
        Permite actualizar un producto buscándolo por su ID.
    """
    try:
        # Llama a ver_productos y comprueba si hay algo para mostrar.
        if not ver_productos(): # Si no hay productos, sale de la función.
            print(Fore.BLUE + '=' * 46)
            print("Volviendo al menú principal.")
            return # Termina la ejecución de la función aquí.
        conexion = obtener_conexion()
        if conexion:
            cursor = conexion.cursor()
            while True:
                id_str = input(Fore.YELLOW + 'Ingrese el ID del producto que desea buscar: ').strip()
                print(Fore.BLUE + '=' * 46) 
                if not id_str:
                    print(Fore.RED + 'El ID no puede estar vacío. Intente de nuevo. ❌')
                    continue
                try:
                    id_producto = int(id_str)
                    break
                except ValueError:
                    print(Fore.RED + 'ID inválido. Por favor, ingrese un número entero. ❌')
                
            while True:
                try:
                    menu_actualizar_producto()
                    entrada_usuario = int(input(Fore.YELLOW + 'Qué campo desea actualizar? Ingrese una opción del menú: '))
                    print(Fore.BLUE+'='*46)
                except ValueError:
                    print(Fore.BLUE+'='*46)
                    print(Fore.RED + 'La opción ingresada no es válida')
                else:
                    match entrada_usuario:
                        case 1:
                            while True:
                                nuevo_nombre = input(Fore.YELLOW + 'Ingrese el nuevo nombre para el producto seleccionado: ').strip().lower()
                                print(Fore.BLUE+'='*46)
                                if not nuevo_nombre:
                                    print(Fore.RED + 'El nombre del producto no puede estar vacío. Inténtelo de nuevo. ❌')
                                    continue
                                else:
                                    query = "UPDATE productos SET nombre = ? WHERE id = ?"
                                    cursor.execute(query, (nuevo_nombre, id_producto))
                                    break
                        case 2:
                            while True:
                                nueva_descripcion = input(Fore.YELLOW + 'Ingrese la nueva descripción para el producto seleccionado: ').strip().lower()
                                print(Fore.BLUE+'='*46)
                                if not nueva_descripcion:
                                    print(Fore.RED + 'La descripción del producto no puede estar vacía. Inténtelo de nuevo. ❌')
                                    continue
                                else:
                                    query = "UPDATE productos SET descripcion = ? WHERE id = ?"
                                    cursor.execute(query, (nueva_descripcion, id_producto))
                                    break
                        case 3:
                            while True:
                                nueva_cantidad = input(Fore.YELLOW + 'Ingrese la nueva cantidad para el producto seleccionado: ').strip()
                                print(Fore.BLUE+'='*46)
                                try:
                                    cantidad = int(nueva_cantidad)
                                    if cantidad < 0:  # Validación de que la cantidad no sea un número negativo.
                                        print(Fore.RED + 'La cantidad no puede ser un número negativo. Inténtelo de nuevo. ❌')
                                    else:
                                        query = "UPDATE productos SET cantidad = ? WHERE id = ?"
                                        cursor.execute(query, (nueva_cantidad, id_producto))
                                        break
                                except ValueError:
                                    print(Fore.RED + 'Cantidad inválida. Por favor, ingrese un número entero. ❌')
                        case 4:
                            while True:
                                nuevo_precio = input(Fore.YELLOW + 'Ingrese el nuevo precio para el producto seleccionado: ').strip()
                                print(Fore.BLUE+'='*46)
                                try: 
                                    precio = float(nuevo_precio)
                                    if precio < 0:
                                        print(Fore.RED + 'El precio no puede ser un número negativo. Inténtelo de nuevo. ❌')
                                    else:
                                        query = "UPDATE productos SET precio = ? WHERE id = ?"
                                        cursor.execute(query, (nuevo_precio, id_producto))
                                        break
                                except ValueError:
                                    print(Fore.RED + 'Precio inválido❗ Por favor, ingrese un número (puede usar decimales).')
                        case 0:
                            print('Volviendo al menú principal...')
                            break
                        case _:
                            print(Fore.BLUE+'='*46)
                            print(Fore.RED + 'La opción ingresada no es válida')
            if cursor.rowcount == 0: # Verifica la cantidad de filas afectadas.
                print(Fore.RED + f'No se encontró el producto con el ID: {id_producto}. ❌')
            else:
                conexion.commit()
                print(Fore.GREEN + f'Producto con ID: {id_producto} modificado con éxito. ✅')
        else:
            print(Fore.RED + 'No se pudo establecer conexión con la base de datos. ❌')
    except sqlite3.Error as e:
        print(Fore.RED + f'Error❗ al conectar con la base de datos: {e}. ❌')
    finally:
        conexion.close()

def eliminar_por_id():
    """
        Permite eliminar un producto buscandolo por su ID.
    """
    try:
        # Llama a ver_productos y comprueba si hay algo para mostrar.
        if not ver_productos(): # Si no hay productos, sale de la función.
            print(Fore.BLUE + '=' * 46)
            print("Volviendo al menú principal.")
            return # Termina la ejecución de la función aquí.
        conexion = obtener_conexion()
        if conexion:
            cursor = conexion.cursor()
            while True:
                id_str = input(Fore.YELLOW + 'Ingrese el ID del producto que desea eliminar: ').strip()
                print(Fore.BLUE + '=' * 46) 
                if not id_str:
                    print(Fore.RED + 'El ID no puede estar vacío. Inténtelo de nuevo. ❌')
                    continue
                try:
                    id_producto = int(id_str)
                    break
                except ValueError:
                    print(Fore.RED + 'ID inválido. Por favor, ingrese un número entero. ❌')

            query = 'DELETE FROM productos WHERE id = ?'
            cursor.execute(query, (id_producto,))

            if cursor.rowcount == 0: # Verifica la cantidad de filas afectadas.
                print(Fore.RED + f'No se encontró el producto con el ID: {id_producto}. ❌')
            else:
                conexion.commit()
                print(Fore.GREEN + f'Producto con ID: {id_producto} eliminado con éxito. ✅')
        else:
            print(Fore.RED + 'No se pudo establecer conexión con la base de datos. ❌')
    except sqlite3.Error as e:
        print(Fore.RED + f'Error❗ al conectar con la base de datos: {e}. ❌')
    finally:
        conexion.close()

def buscar_por_stock():
    """
        Permite buscar que productos con un stock menor al ingresado por el usuario.
    """
    try:
        conexion = obtener_conexion()
        if conexion:
            cursor = conexion.cursor()
            while True:
                stock_min_str = input(Fore.YELLOW + 'Ingrese una cantidad para filtrar los productos con stock inferior al mismo: ').strip()
                print(Fore.BLUE+'='*46)
                try:
                    stock_min = int(stock_min_str) # Intenta convertir a entero
                    if stock_min < 0:
                        print(Fore.RED + 'La cantidad no puede ser un número negativo. Inténtelo de nuevo. ❌')
                        continue # Vuelve a pedir la entrada
                    else:
                        break
                except ValueError:
                    print(Fore.RED + 'Cantidad inválida. Por favor, ingrese un número entero. ❌')
                    continue # Vuelve a pedir la entrada
                
            query = 'SELECT * FROM productos WHERE cantidad < ?'
            cursor.execute(query,(stock_min,))
            productos = cursor.fetchall()
            if not productos:
                print(Fore.RED + 'No hay productos almacenados. ❌') 
            else:
                ancho_id = 10
                ancho_nombre = 20 
                ancho_descripcion = 30 
                ancho_cantidad = 12
                ancho_precio = 12

                header = (
                    Fore.LIGHTCYAN_EX + 
                    f'| {'ID':^{ancho_id}} '
                    f'| {'NOMBRE':^{ancho_nombre}} '
                    f'| {'DESCRIPCION':^{ancho_descripcion}} '
                    f'| {'CANTIDAD':^{ancho_cantidad}} '
                    f'| {'PRECIO':^{ancho_precio}} |'
                    ) 
                print(Fore.LIGHTCYAN_EX + '-' * (len(header)-5)) # Línea separadora superior del encabezado de la tabla.
                print(header)                                    # Imprime el encabezado de la tabla.
                print(Fore.LIGHTCYAN_EX + '-' * (len(header)-5)) # Línea separadora inferior del encabezado de la tabla.
                
                for producto in productos:
                    precio_formateado = f'{producto[4]:.2f}' # Formatea el precio a 2 decimales.
                    nombre_recortado = (str(producto[1])[:ancho_nombre]).ljust(ancho_nombre) # Recorta el nombre al ancho máximo proporcionado.
                    descripcion_recortada = (str(producto[2])[:ancho_descripcion]).ljust(ancho_descripcion) # Recorta la descripción al máximo proporcionado.
                    print(
                        f'| {producto[0]:^{ancho_id}} '             # ID alineado al centro.
                        f'| {nombre_recortado.title()} '            # Nombre alineado a la izquierda.
                        f'| {descripcion_recortada.title()} '       # Descripción alineada a la izquierda.
                        f'| {producto[3]:^{ancho_cantidad}} '       # Cantidad alineada al centro.
                        f'| {precio_formateado:>{ancho_precio}} |'  # Precio alineado a la derecha.
                    )
                print(Fore.LIGHTCYAN_EX + '-' * (len(header) - 5)) # Línea final de la tabla.

        else:
            print(Fore.RED + 'No se pudo establecer conexión con la base de datos. ❌')
    except sqlite3.Error as e:
        print(Fore.RED + f'Error❗ al conectar con la base de datos: {e}. ❌')
    finally:
        conexion.close()