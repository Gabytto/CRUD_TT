from colorama import Fore, init, Style
init(autoreset=True)

def menu_principal():
    '''
    Muestra el menú principal
    '''
    print(Fore.BLUE+'='*20, Fore.YELLOW+'MENU',Fore.BLUE+ '='*20),
    print('1. Gestionar clientes'),
    print('2. Gestionar productos'),
    print('3. Salir'),
    print(Fore.BLUE+'='*46)
    
    
    
    