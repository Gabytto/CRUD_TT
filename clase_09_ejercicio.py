'''
¡Hola! Tu tarea es crear un programa en Python con las siguientes características: 

Agregar productos: Permite agregar productos a una lista. Cada producto debe tener un nombre y un precio

Consultar productos: Muestra todos los productos en la lista junto con sus precios.

Eliminar productos: Elimina un producto de la lista a partir de su nombre.

Menú interactivo: El programa debe ofrecer un menú para que se pueda elegir qué acción realizar. 
Debe incluirse una opción para salir del programa.
'''
# Variables globales
activo = True
continuar = True
productos = []

# Definición de funciones
def mostrar_menu():
    print('='*20, 'MENU', '='*20),
    print('1. Agregar prodcutos'),
    print('2. Ver prodcutos'),
    print('3. Eliminar producto'),
    print('0. Salir'),
    print('='*46)

def agregar_productos():
    producto_nuevo = []
    nombre_producto = input('Ingrese el nombre del producto: ')
    precio_producto = input('Ingrese el precio del producto: ')
    producto_nuevo.append(nombre_producto)
    producto_nuevo.append(precio_producto)
    productos.append(producto_nuevo)
    print('El producto se ha agregado satisfactoriamente!')

def consultar_productos():
    pass

def eliminar_productos():
    pass

def validar_entrada(dato_usuario):
    if dato_usuario.isdigit():
        return int(dato_usuario)
    else:
        return -1



# Inicio del ciclo

while activo:
    mostrar_menu()

    entrada_usuario = input('Ingrese una opcion del menú: ')
    opcion_elegida = validar_entrada(entrada_usuario)

    match opcion_elegida:
        case 1:
            while continuar:
                agregar_productos()
                pregunta = input('Desea continuar agregando?(si/no)').lower()
                if pregunta == 'si':
                    continue
                elif pregunta == 'no':
                    print('Volviendo al menu principal... ')
                    continuar = False
        case 2:
            consultar_productos()
        case 3:
            eliminar_productos()
        case 0:
            print('Saliendo del sistema...')
            activo = False
        case _:
            print('El valor ingresado no es el esperado, intenta nuevamente: ')
            continue