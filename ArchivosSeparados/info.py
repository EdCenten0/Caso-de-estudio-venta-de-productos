import os

def info(nombreProducto, precioProducto, cVendida, total):
    print("**** Mostrará la información ****")
    print("Nombre del producto: "+"\t"+"Precio producto: "+"\t"+"Cantidad de producto vendida: "+"\t"+"Total: ")  
    for a, b, c, d in zip(nombreProducto, precioProducto, cVendida, total):
        print(a+"\t\t\t\t"+str(b)+"\t\t\t"+str(c)+"\t\t\t"+str(d))
        
    os.system("pause")
    os.system("cls")
    print()
    return nombreProducto, precioProducto, cVendida, total