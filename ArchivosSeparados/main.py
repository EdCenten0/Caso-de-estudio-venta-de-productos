from menu import menu

nombreProducto = []
precioProducto = []
cVendida = []
total = []

def main(nombreProducto, precioProducto, cVendida, total):
    menu(nombreProducto, precioProducto, cVendida, total)
    return nombreProducto, precioProducto, cVendida, total

main(nombreProducto, precioProducto, cVendida, total)
