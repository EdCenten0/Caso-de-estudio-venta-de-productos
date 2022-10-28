
def agregar(nombreProducto, precioProducto, cVendida, total):
    print("**** Agregará un producto ****") 
    prod = input("Ingrese el nombre del producto: ")
    nombreProducto.append(prod)
    prec = int(input("Digite el precio del producto C$: "))
    precioProducto.append(prec)
    total.append(0)
    cVendida.append(0)

    return nombreProducto, precioProducto, cVendida, total
    