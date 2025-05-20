#VARIABLES
productos = []    
entrada = ''

activo = True

#COMIENZO DEL CICLO
while activo:

    #MENU INICIAL
    
    print('='*20, 'MENU', '='*20),
    print('1. Agregar prodcutos'),
    print('2. Ver prodcutos'),
    print('3. Buscar producto'),
    print('4. Actualizar producto'),
    print('5. Eliminar producto'),
    print('0. Salir'),
    print('='*46)
   

    #SOLICITAR INPUT

    entrada = input('Ingrese una opción del menú: ')

    #COMPROBACIÓN DE TIPO DE DATO INGRESADO

    if entrada.isdigit():
        entrada = int(entrada)
    else:
        print('Haz ingresado un carácter no válido.')
        continue
    
    if entrada < 0 or entrada > 5:
        print('Haz ingresado un carácter no válido.')

    #1. AGREGAR UN PRODUCTO
    if entrada == 1:
        agregando_productos = True
        while agregando_productos:
            producto = []
            print('-'*46)
            nombre_producto = input('0. Volver al menú principal \nIngrese el nombre del producto a agregar: ').lower()
            if nombre_producto == '0':
                print('='*46)
                print('volviendo al menú principal...')
                agregando_productos = False
                continue
            categoria_producto = input('Ingreses a que categoría pertenece el producto: ')
            precio_producto = ''
            while precio_producto.isdigit() == False:
                precio_producto = input('Ingrese el precio del producto sin centavos: ')
                
            if precio_producto.isdigit():
                precio_producto = int(precio_producto)
            
            producto.append(nombre_producto)
            producto.append(categoria_producto)
            producto.append(precio_producto)
            productos.append(producto)
            print('-'*46)
            print(f'Producto agregado con éxito!: {producto[0].title()}')
            

            precio_producto = '' #vuelvo a poner precio en str

    #2. VER PRODUCTOS
    elif entrada == 2:
        if productos == []:
            print('No se encontraron productos.')
        else: 
            print('-'*46)
            print('\nProductos registrados:')
            for i in range(len(productos)):
                producto = productos[i]
                print('-'*46)
                print(f'Producto {i+1}: ')
                print(f'Nombre del producto: {producto[0].title()}')
                print(f'Categoría: {producto[1]}')
                print(f'Precio: {producto[2]}')
                print('-'*46)

    #3. BUSCAR UN PRODUCTO
    elif entrada == 3:
        print('-'*46)
        registro = input('Ingresa el nombre del producto a buscar: ')
        for producto in productos:
            if registro in producto[0]:
                print('-'*46)
                print(f'Producto encontrado: ')
                print(f'Nombre del producto: {producto[0].title()}')
                print(f'Categoría: {producto[1]}')
                print(f'Precio: {producto[2]}')
                print('-'*46)
            else:
                print('-'*46)
                print('Producto no encontrado.')
                continue
     
    #4.ACTUALIZAR UN PRODUCTO

    elif entrada == 4:
        print('-'*46)
        registro = input('Ingresa el numero del producto a modificar: ')
        if registro.isdigit():
            registro = int(registro)
        else:
            print('Haz ingresado un carácter no válido.')
            continue
        producto = []
        nombre_producto_nuevo = input('Ingrese el nombre del producto: ').lower()
        categoria_producto_nuevo = input('Ingreses a que categoría pertenece el producto: ')
        precio_producto_nuevo = ''
        while precio_producto_nuevo.isdigit() == False:
            precio_producto_nuevo = input('Ingrese el precio del producto sin centavos: ')
        if precio_producto_nuevo.isdigit():
            precio_producto_nuevo = int(precio_producto_nuevo)
        productos.pop(registro-1)
        producto.append(nombre_producto_nuevo)
        producto.append(categoria_producto_nuevo)
        producto.append(precio_producto_nuevo)
        productos.insert(registro-1, producto)
        print('-'*46)
        print('El producto de ha modificado exitosamente: ')
        print(f'\nNombre del producto: {producto[0].title()}')
        print(f'Categoría: {producto[1]}')
        print(f'Precio: {producto[2]}')




    #5. ELIMINAR UN PRODUCTO

    elif entrada == 5:
        print('-'*46)
        registro = input('Ingresa el numero del producto a eliminar: ')
        if registro.isdigit():
            registro = int(registro)
        else:
            print('Haz ingresado un carácter no válido.')
            continue
        producto_eliminado = productos.pop(registro-1)
        print('='*46)
        print('El producto: \n', producto_eliminado[0].title(), '\nha sido eliminado satisfactoriamente.')

    #0. SALIR
    elif entrada == 0:
        print('Saliendo del sistema...')
        print('='*46)
        activo = False


#probandooooo

   