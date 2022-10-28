

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