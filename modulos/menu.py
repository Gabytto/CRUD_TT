from colorama import Fore, init, Style
init(autoreset=True)

def menu_principal():
    '''
        Muestra el menú principal de la aplicación.
    '''
    print(Fore.BLUE+'='*15, Fore.YELLOW+'MENU PRINCIPAL',Fore.BLUE+ '='*15),
    print('1. Agregar productos.'),
    print('2. Ver todos los productos.'),
    print('3. Busqueda de producto por ID.'),
    print('4. Actualizar productos por ID.'),
    print('5. Eliminar producto por ID.'),
    print('6. Buscar productos por stock.')
    print('0. Salir del programa.'),
    print(Fore.BLUE+'='*46)
    
def menu_actualizar_producto():
    """
        Muestra el menú de selección del campos a modificar en un registro ya almacenado.
    """
    print(Fore.BLUE+'='*12, Fore.YELLOW+'ACTUALIZAR  PRODUCTO',Fore.BLUE+ '='*12),
    print('1. Nombre del producto.'),
    print('2. Descripción del producto.'),
    print('3. Cantidad en stock.'),
    print('4. Precio del producto.'),
    print('0. Volver al menú anterior.'),
    print(Fore.BLUE+'='*46)