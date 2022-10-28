

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