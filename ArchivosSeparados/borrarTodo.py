

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