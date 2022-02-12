class Factura:


producto=""
cantidad=0
precio=0.0
total=0.0


#1) ingresar Datos
#2) Procesar Datos
#3) MOstrar Resultados

def ingresar_datos():
    global cantidad,precio,total


    cantidad=int(input("ingresar Cantidad: "))
    precio = float (input)