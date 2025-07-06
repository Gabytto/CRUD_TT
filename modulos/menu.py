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
    
    
    
    