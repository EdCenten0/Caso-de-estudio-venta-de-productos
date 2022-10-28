from agregar import agregar
from borrar import borrar
from borrarTodo import borrarTodo
from info import info
from venta import venta

# Menú de funciones
def menu(nombre, precio, cantidad, totalidad):
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

        # Agregar los productos.
        if(opc==1):
                 
            agregar(nombre, precio, cantidad, totalidad)
            
        # Realizar la venta.
        elif(opc==2):
            venta(nombre, precio, cantidad, totalidad)

        # Borrar un producto.
        elif(opc==3):
            borrar(nombre, precio, cantidad, totalidad)

        # Borrar todos los productos de la venta.
        elif(opc==4):
            borrarTodo(nombre, precio, cantidad, totalidad)

        # Mostrar los elementos de la venta.
        elif(opc==5):
            info(nombre, precio, cantidad, totalidad)
            
        # Salir del programa.
        elif(opc==6):
            print("**** Usted ha salido del programa ****")
            break

        else:
            print("Digite una opcion valida!!")
            print()

    return nombre, precio, cantidad, totalidad