from colorama import Fore, init, Style
from modulos.menu import menu_principal
from modulos.productos import (agregar_productos, 
                               ver_productos, 
                               busqueda_por_id, 
                               actualizar_por_id, 
                               eliminar_por_id,
                               buscar_por_stock
                               )
init(autoreset=True)

# Variables globales
programa_activo = True

# Comienzo del ciclo
while programa_activo:
    menu_principal()

    try:
        entrada_usuario = int(input(Fore.YELLOW + 'Ingrese una opción del menú: '))
        print(Fore.BLUE+'='*46)
    except ValueError:
        print(Fore.BLUE+'='*46)
        print(Fore.RED + 'La opción ingresada no es válida')
    else:    
        match entrada_usuario:
            case 1:
                agregar_productos()
            case 2:
                ver_productos()
            case 3:
                busqueda_por_id()
            case 4:
                actualizar_por_id()
            case 5:
                eliminar_por_id()
            case 6:
                buscar_por_stock()
            case 0:
                print('Saliendo del programa...')
                programa_activo = False
            case _:
                print(Fore.BLUE+'='*46)
                print(Fore.RED + 'La opción ingresada no es válida')
    


