from colorama import Fore, init, Style
from modulos.menu import menu_principal, menu_clientes

# Variables globales
programa_activo = True

# Comienzo del ciclo
while programa_activo:
    menu_principal()

    try:
        entrada_usuario = int(input(Fore.YELLOW + 'Ingrese una opción del menú: '))
    except ValueError:
        print(Fore.BLUE+'='*46)
        print(Fore.RED + 'La opción ingresada no es válida')
    else:    
        match entrada_usuario:
            case 1:
                menu_clientes()
                
            case 2:
                pass
                #menu_productos()
            case 0:
                print('Saliendo del programa...')
                programa_activo = False
            case _:
                print(Fore.BLUE+'='*46)
                print(Fore.RED + 'La opción ingresada no es válida')
    


