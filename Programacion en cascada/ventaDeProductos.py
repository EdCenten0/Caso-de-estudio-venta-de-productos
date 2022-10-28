'''
Algoritmo de caso de estudio de venta de productos
Clase: ALgoritmos y estructuras de datos
Hecho por: Carlos Eduardo Chavarria Centeno
28-10-22.

'''

from os import remove
import os



# Listas:
nombreProducto = []
precioProducto = []
cVendida = []
total = []





'''
Menú de funciones.
'''
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
        print("**** Agregará un producto ****")
        print() 
        
        prod = input("Ingrese el nombre del producto: ")
        nombreProducto.append(prod)
        prec = int(input("Digite el precio del producto C$: "))
        precioProducto.append(prec)
        total.append(0)
        cVendida.append(0)
        
            
        print()      
     
        
    # Realizar la venta
    elif(opc==2):
        print("****Realizará una venta ****")
        np = input("Ingrese el nombre del producto que desea comprar: ")

        if np in nombreProducto:
            ind = nombreProducto.index(np)
            cvp = int(input("Ingrese la cantidad de producto a comprar: "))

            res = cvp * precioProducto[ind]
            
            print("Su total es: ", res)

            
            
            
            
            total[ind] = total[ind] + res
            
            cVendida[ind] = cVendida[ind] + cvp
            print()
                
        else:
            print("Producto no encontrado!!")
            print()
                

    # Borrar un producto.
    elif(opc==3):
        print("**** Borrará un producto****")
        pBorrar = input("Ingrese el nombre del producto que desea elimar: ")
        
        if pBorrar in nombreProducto:
            ind = nombreProducto.index(pBorrar)
            n = nombreProducto.pop(ind)
            precioProducto.pop(ind)
            cVendida.pop(ind)
            total.pop(ind)
            
            print(f"Elemento eliminado: {n}")
        else:
            print("No se encuentra ese elemento!!")

    # Borrar todos los productos de la venta.
    elif(opc==4):
        print("**** Borrará todos los productos ****")
        nombreProducto.clear()
        precioProducto.clear()
        cVendida.clear()
        total.clear()
        
        if nombreProducto==[] and precioProducto==[] and cVendida==[] and total==[]:
            print("Datos eliminados con exito!!")
        else:
            print("Error al eliminar los productos")

    # Mostrar los elementos de la venta.
    elif(opc==5):
            print("**** Mostrará la información ****")
            print("Nombre del producto: "+"\t"+"Precio producto: "+"\t"+"Cantidad de producto vendida: "+"\t"+"Total: ")
    
    

            for a, b, c, d in zip(nombreProducto, precioProducto, cVendida, total):
                print(a+"\t\t\t\t"+str(b)+"\t\t\t"+str(c)+"\t\t\t"+str(d))

            os.system("pause")
            os.system("cls")
            print()
        
    # Salir del programa.
    elif(opc==6):
        print("**** Usted ha salido del programa ****")
        break

    else:
        print("Digite una opcion valida!!")
        print()


