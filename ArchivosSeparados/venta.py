

def venta(nombre, precio, cantidad, totalidad):
    print("****Realizará una venta ****")
    np = input("Ingrese el nombre del producto que desea comprar: ")

    if np in nombre:
        ind = nombre.index(np)
        cvp = int(input("Ingrese la cantidad de producto a comprar: "))
        res = cvp * precio[ind]
        print("Su total es: ", res)
        totalidad[ind] = totalidad[ind] + res
        cantidad[ind] = cantidad[ind] + cvp
        print()
    else:
        print("Producto no encontrado!!")
        
                    

    return nombre, precio, cantidad, totalidad