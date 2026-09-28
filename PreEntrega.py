productos=[]

while True :

    print("\n" "*****MENU*****")
    print("\n" "1_Ingrese productos")
    print("\n" "2_Borrar producto")

    opciones=input("\n""Seleccione una Opcion, 5-salir")

    match opciones:
        case "1":
            nombre=input("\n ingrese nombre del producto ")
            if nombre == "":
                print("Error nombre de producto incorrecto")
                continue
            else :
               productos.append(nombre)
               print(f"\n el producto: {nombre.capitalize()} agregado correctamente")
        case "3":
            nombre=input("\n ingrese nombre del producto que desea borrar ")
            if nombre == "nombre":
                productos.remove(nombre)
                print(f"\n el producto: {nombre} borrado correctamente")
            else :
                print("Error nombre de producto inexistente intente nuevamente")
        case "5":
            print("\n Gracias por usar nuestro menu")
            break