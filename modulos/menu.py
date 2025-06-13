from colorama import Fore, init, Style
init(autoreset=True)

def menu_principal():
    '''
    Muestra el menú principal
    '''
    print(Fore.BLUE+'='*15, Fore.YELLOW+'MENU PRINCIPAL',Fore.BLUE+ '='*15),
    print('1. Gestionar clientes'),
    print('2. Gestionar productos'),
    print('0. Salir'),
    print(Fore.BLUE+'='*46)

def menu_clientes():
    '''
    Muestra el menú de opciones al seleccionar "1. Gestionar clientes"
    en el menú principal.
    '''
    print(Fore.BLUE+'='*15, Fore.YELLOW+'MENU CLIENTES',Fore.BLUE+ '='*15),
    print('1. Agregar clientes'),
    print('2. Ver todos los clientes'),
    print('3. Buscar un cliente'),
    print('4. Modificar cliente'),
    print('5. Eliminar cliente'),
    print('0. Volver al manú anterior'),
    print(Fore.BLUE+'='*46)
    
    
    
    