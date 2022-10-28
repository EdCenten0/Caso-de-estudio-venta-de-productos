from menu import menu

nombreProducto = []
precioProducto = []
cVendida = []
total = []

def main(nombre, precio, cantidad, totalidad):
    menu(nombreProducto, precioProducto, cVendida, total)
    return nombre, precio, cantidad, totalidad

main(nombreProducto, precioProducto, cVendida, total)
