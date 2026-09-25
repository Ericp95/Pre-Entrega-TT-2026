productos=[]

while True :

    print("\n" "*****MENU*****")
    print("\n" "1_Ingrese productos")

    opciones=input("\n""Seleccione una Opcion, 5-salir")

    match opciones:
        case "1":
            nombre=input("ingrese nombre del producto ")
            productos.append(nombre)
        case "5":
            print("\n Gracias por usar nuestro menu")
            break