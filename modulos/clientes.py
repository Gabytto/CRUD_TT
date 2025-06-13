from colorama import Fore, init, Style
init(autoreset=True)

def agregar_clientes():
    '''
    Sirve para agregar clientes al sistema.
    '''
    cliente = []
    nombre_cliente = input(Fore.YELLOW + 'Ingrese el nombre del cliente: ')
    print(Fore.BLUE+'='*46)
    mail_cliente = input(Fore.YELLOW + 'Ingrese el e-mail del cliente: ')
    cliente.append(nombre_cliente)
    cliente.append(mail_cliente)
    print(Fore.BLUE+'='*46)
    print(Fore.GREEN + f'Cliente: {cliente[0]} agregado con éxito! ')
