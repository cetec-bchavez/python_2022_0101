cantidad=0
precio=0.0
total=0.0

#1) Ingresar Datos
#2) Procesar Datos
#3) Mostrar Resultados

def ingresar_datos():
    global cantidad,precio,total

    cantidad = int(input('Ingresar Cantidad: '))
    precio = float(input('Ingresar Precio: '))

def procesar_datos():
    global cantidad,precio,total

    total=cantidad * precio

def mostrar_resultados():
    global cantidad,precio,total
    print('Total=',total)


ingresar_datos()
procesar_datos()
mostrar_resultados()