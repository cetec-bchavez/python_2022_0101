cantidad = 0
precio = 0
total = 0

# ingreso de datos

def ingresar_datos():
    global cantidad,precio,total
    
    cantidad = int(input('ingrese cantidad: '))
    precio = float(input('ingrese precio: '))
    
# procesar

def procesar_datos():
    global cantidad,precio,total
    total = cantidad * precio
    
# resultado
    
def mostrar_resultado():
    global cantidad,precio,total
    print('Total =',total)
    
ingresar_datos()
procesar_datos()
mostrar_resultado()

