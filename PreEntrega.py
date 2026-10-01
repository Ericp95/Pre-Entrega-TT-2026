productos=[]

while True :

    print("\n" "*****MENU*****")
    print("\n" "1_Ingrese productos")
    print("\n" "2_Borrar producto")
    print("\n" "3_Lista de Productos")
    print("\n" "4_Busqueda de producto")
    print("\n" "5_Salir")
    print("\n" "**********")


    opciones=input("\n""Seleccione una Opcion")

    match opciones:
        case "1":
            print("\n" "*************")
            nombre=input("\n ingrese nombre del producto ")
            if nombre == "":
                print("\n Error nombre de producto incorrecto")
                #continue
            else :
               productos.append(nombre)
               print(f"\n el producto: {nombre.title()} agregado correctamente")
        case "2":
            print("\n" "*************")
            nombre=input("\n ingrese nombre del producto que desea borrar ")
            if nombre in productos:
                productos.remove(nombre)
                print(f"\n el producto: {nombre.capitalize()} borrado correctamente")
            else :
                print("Error nombre de producto inexistente intente nuevamente")
        case "3":
            print("\n *****Listado de Productos*****")
            for producto in productos:
             print(producto.title())
            print("\n" "*************")
        case "4":
            print("\n" "*************")
            nombre=input("\n ingrese nombre de producto a buscar")
            if nombre in productos:
                print(f"\n el producto con el nombre: {nombre.title()}, esta en stock")
            else:
                print("\n el producto no esta en stock")
            
        case "5":
            print("\n" "*************")
            print("\n Gracias por usar nuestro menu")
            print("\n" "*************")
            break