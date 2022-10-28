# Se borra un producto.
def borrar(nombre, precio, cantidad, totalidad):
    print("**** Borrará un producto****")
    pBorrar = input("Ingrese el nombre del producto que desea elimar: ")
            
    if pBorrar in nombre:
        ind = nombre.index(pBorrar)
        n = nombre.pop(ind)
        precio.pop(ind)
        cantidad.pop(ind)
        totalidad.pop(ind)
                
        print(f"Elemento eliminado: {n}")
    else:
        print("No se encuentra ese elemento!!")

    return nombre, precio, cantidad, totalidad