import os

# Se muestra la informacion de todos los productos.
def info(nombre, precio, cantidad, totalidad):
    print("**** Mostrará la información ****")
    print("Nombre del producto: "+"\t"+"Precio producto: "+"\t"+"Cantidad de producto vendida: "+"\t"+"Total: ")  
    for a, b, c, d in zip(nombre, precio, cantidad, totalidad):
        print(a+"\t\t\t\t"+str(b)+"\t\t\t"+str(c)+"\t\t\t"+str(d))
        
    os.system("pause")
    os.system("cls")
    print()
    return nombre, precio, cantidad, totalidad