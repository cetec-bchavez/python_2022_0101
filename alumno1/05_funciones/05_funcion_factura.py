
cantidad=0
precio=0.0
total=0.0

#ingresar datos
#procesar datos
#mostrar resultados

def ingresar_datos():   
    global cantidad,precio,total

    cantidad= int(input('ingresar cantidad: '))
    precio= float(input('ingresar precio: '))

def procesar_datos():   
    global cantidad,precio,total

    total=cantidad * precio

def mostrar_resultados():   
    global cantidad,precio,total   
    print('Total: ',total)

ingresar_datos()
procesar_datos()
mostrar_resultados()
