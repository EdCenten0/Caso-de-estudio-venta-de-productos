# Se borran todos los productos.
def borrarTodo(nombre, precio, cantidad, totalidad):
    print("**** BorrarĂ¡ todos los productos ****")
    nombre.clear()
    precio.clear()
    cantidad.clear()
    totalidad.clear()
    
    if nombre==[] and precio==[] and cantidad==[] and totalidad==[]:
        print("Datos eliminados con exito!!")
    else:
        print("Error al eliminar los productos")
    
    return nombre, precio, cantidad, totalidad