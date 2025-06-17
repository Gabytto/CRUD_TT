from colorama import Fore, init, Style
init(autoreset=True)

# Variables globales
clientes = []

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
        clientes.append(cliente)

        print(Fore.BLUE+'='*46)
        print(Fore.GREEN + f'Cliente: {cliente[0]} agregado con éxito! ')
        print(Fore.BLUE+'='*46)
        continuar_agregando = input(Fore.YELLOW + 'Desea continuar agregando clientes? (s/n): ').lower()
        if continuar_agregando == 's':
            print(Fore.BLUE+'='*46)
            continue
        elif continuar_agregando == 'n':
            print(Fore.BLUE+'='*46)
            print('Volviendo al menú principal...')
            agregando_clientes = False
        else:
            print(Fore.BLUE+'='*46)
            print(Fore.RED + 'La opción ingresada no es válida')
            print(Fore.BLUE+'='*46)

def ver_clientes():
    '''
    Sirve para consultar el listado de clientes completo.
    '''
    if not clientes:
        print(Fore.BLUE+'='*46)
        print(Fore.RED + 'No hay clientes para mostrar.')
    else: 
        print(Fore.BLUE+'='*12, Fore.YELLOW+'LISTADO DE CLIENTES',Fore.BLUE+ '='*12)
        for i in range(len(clientes)):
            cliente = clientes[i]
            print(f'Cliente ID: {i+1} ')
            print(f'Nombre y apellido: {cliente[0].title()}')
            print(f'E-mail: {cliente[1]}')
            print(Fore.BLUE+'-'*46)