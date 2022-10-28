
def agregar(nombre, precio, cantidad, totalidad):
    print("**** Agregará un producto ****") 
    prod = input("Ingrese el nombre del producto: ")
    nombre.append(prod)
    prec = int(input("Digite el precio del producto C$: "))
    precio.append(prec)
    totalidad.append(0)
    cantidad.append(0)

    return nombre, precio, cantidad, totalidad
    