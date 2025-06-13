from colorama import Fore, init, Style
from modulos.menu import menu_principal

# Variables globales
programa_activo = True

# Comienzo del ciclo
while programa_activo:
    menu_principal()

    entrada_usuario = int(input(Fore.YELLOW + 'Ingrese una opción del menú: '))
    match entrada_usuario:
        case 1:
            pass
            #menu_clientes()
        case 2:
            pass
            #menu_productos()
        case 3:
            print('Saliendo del programa...')
            programa_activo = False

