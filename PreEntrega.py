productos=[]

while True :

    print("\n" "*****MENU*****")
    print("\n" "1_Ingrese productos")

    opciones=input("\n""Seleccione una Opcion, 5-salir")

    match opciones:
        case "1":
            nombre=input("\n ingrese nombre del producto ")
            if nombre == "":
                print("Error nombre de producto incorrecto")
                continue
            else :
               productos.append(nombre)
               print(f"\n el producto: {nombre} agregado correctamente")
        case "5":
            print("\n Gracias por usar nuestro menu")
            break