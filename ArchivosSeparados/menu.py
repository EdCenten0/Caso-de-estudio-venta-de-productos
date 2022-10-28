from agregar import agregar
from borrar import borrar
from borrarTodo import borrarTodo
from info import info
from venta import venta

def menu(nombreProducto, precioProducto, cVendida, total):
    while True:
        print("------- Bienvenido a la venta --------")
        print("1. Agregar un producto")
        print("2. Realizar una venta")
        print("3. Borrar un producto")
        print("4. Borrar todos los productos")
        print("5. Mostrar informacion")
        print("6. Salir")
        opc = int(input("Digite la opcion que desee: "))
        print()

        #Agregar los productos
        if(opc==1):
                 
            agregar(nombreProducto, precioProducto, cVendida, total)
            
        #Realizar la venta
        elif(opc==2):
            venta(nombreProducto, precioProducto, cVendida, total)

        #Borrar un producto
        elif(opc==3):
            borrar(nombreProducto, precioProducto, cVendida, total)

        #Borrar todos los productos de la venta
        elif(opc==4):
            borrarTodo(nombreProducto, precioProducto, cVendida, total)

        #Mostrar los elementos de la venta
        elif(opc==5):
            info(nombreProducto, precioProducto, cVendida, total)
            
            #Salir del programa
        elif(opc==6):
            print("**** Usted ha salido del programa ****")
            break

        else:
            print("Digite una opcion valida!!")
            print()

    return nombreProducto, precioProducto, cVendida, total