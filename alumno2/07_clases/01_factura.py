class Factura:     #la primera debe ser mayuscula en class para diferenciar de objetos
    producto=""
    cantidad=0
    precio=0
    total=0

    def __init__(self,productox,cantidadx,preciox,totalx):
        
        self.producto=productox
        self.candidad=cantidadx
        self.precio=preciox
        self.total=totalx

factura1= Factura("mouse",5,8,0)

#cambiar nombre a algo ya puesto, apuntar a una celda de la fila que queremos
factura1.producto="mouse genius"
print (factura1.producto,factura1.total)

factura2= Factura("teclado",5,2,0)
print (factura2.producto,factura2.total)

facturas=[]          #creamos un array

facturas.append(factura1)   #añadimos TODA la fila de factura 1 a facturas
facturas.append(factura2)

print("unir todos los datos")

for facturax in facturas:
    print(facturax.producto,facturax.total)


