'''
Algoritmo de caso de estudio de venta de productos
Clase: ALgoritmos y estructuras de datos
Hecho por: Carlos Eduardo Chavarria Centeno
28-10-22.

'''

from menu import menu

nombreProducto = []
precioProducto = []
cVendida = []
total = []

# La funcion principal main.
def main(nombre, precio, cantidad, totalidad):
    menu(nombreProducto, precioProducto, cVendida, total)
    return nombre, precio, cantidad, totalidad

main(nombreProducto, precioProducto, cVendida, total)
