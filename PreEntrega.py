productos=[]

while True :

    print("\n" "*****MENU*****")
    print("\n" "1_Ingrese productos")
    print("\n" "2_Borrar producto")
    print("\n" "3_Lista de Productos")
    print("\n" "5_Salir")


    opciones=input("\n""Seleccione una Opcion")

    match opciones:
        case "1":
            nombre=input("\n ingrese nombre del producto ")
            if nombre == "":
                print("Error nombre de producto incorrecto")
                continue
            else :
               productos.append(nombre)
               print(f"\n el producto: {nombre.capitalize()} agregado correctamente")
        case "2":
            nombre=input("\n ingrese nombre del producto que desea borrar ")
            if nombre == "nombre":
                productos.remove(nombre)
                print(f"\n el producto: {nombre} borrado correctamente")
            else :
                print("Error nombre de producto inexistente intente nuevamente")
        case "3":
            for nombres in productos:
                print(productos)
        case "5":
            print("\n Gracias por usar nuestro menu")
            break