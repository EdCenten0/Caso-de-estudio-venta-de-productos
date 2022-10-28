from os import remove
import os

from numpy import empty

#Listas:
nombreProducto = []
precioProducto = []
cVendida = []
total = []


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
    

def agregar(nombreProducto, precioProducto, cVendida, total):
    print("**** Agregará un producto ****") 
    prod = input("Ingrese el nombre del producto: ")
    nombreProducto.append(prod)
    prec = int(input("Digite el precio del producto C$: "))
    precioProducto.append(prec)
    total.append(0)
    cVendida.append(0)

    return nombreProducto, precioProducto, cVendida, total
    

def venta(nombreProducto, precioProducto, cVendida, total):
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
        
                    

    return nombreProducto, precioProducto, cVendida, total
    

def borrar(nombreProducto, precioProducto, cVendida, total):
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

    return nombreProducto, precioProducto, cVendida, total

def borrarTodo(nombreProducto, precioProducto, cVendida, total):
    print("**** Borrará todos los productos ****")
    nombreProducto.clear()
    precioProducto.clear()
    cVendida.clear()
    total.clear()
    #cantidadProducto.clear()
    if nombreProducto==[] and precioProducto==[] and cVendida==[] and total==[]:
        print("Datos eliminados con exito!!")
    else:
        print("Error al eliminar los productos")
    
    return nombreProducto, precioProducto, cVendida, total

def info(nombreProducto, precioProducto, cVendida, total):
    print("**** Mostrará la información ****")
    print("Nombre del producto: "+"\t"+"Precio producto: "+"\t"+"Cantidad de producto vendida: "+"\t"+"Total: ")  
    for a, b, c, d in zip(nombreProducto, precioProducto, cVendida, total):
        print(a+"\t\t\t\t"+str(b)+"\t\t\t"+str(c)+"\t\t\t"+str(d))
        
    os.system("pause")
    os.system("cls")
    print()
    return nombreProducto, precioProducto, cVendida, total

def main(nombreProducto, precioProducto, cVendida, total):
    menu(nombreProducto, precioProducto, cVendida, total)
    return nombreProducto, precioProducto, cVendida, total

main(nombreProducto, precioProducto, cVendida, total)