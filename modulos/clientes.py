from colorama import Fore, init, Style
init(autoreset=True)

def agregar_clientes():
    '''
    Sirve para agregar clientes al sistema.
    '''
    agregando_clientes = True

    while agregando_clientes:
        cliente = []
        nombre_cliente = input(Fore.YELLOW + 'Ingrese el nombre del cliente: ')
        print(Fore.BLUE+'='*46)
        mail_cliente = input(Fore.YELLOW + 'Ingrese el e-mail del cliente: ')
        cliente.append(nombre_cliente)
        cliente.append(mail_cliente)
        print(Fore.BLUE+'='*46)
        print(Fore.GREEN + f'Cliente: {cliente[0]} agregado con éxito! ')
        print(Fore.BLUE+'='*46)
        continuar_agregando = input(Fore.YELLOW + 'Desea continuar agregando cliente? (s/n): ').lower()
        if continuar_agregando == 's':
            print(Fore.BLUE+'='*46)
            continue
        elif continuar_agregando == 'n':
            print(Fore.BLUE+'='*46)
            print('Volviendo al menú principal...')
            agregando_clientes = False
        else:
            print(Fore.RED + 'La opción ingresada no es válida')
