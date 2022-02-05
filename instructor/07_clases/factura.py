class Factura:
    #Variables Columnas, Variables Complejas
    producto=''
    cantidad=0
    precio=0.0
    total=0.0

    def __init__(self,productox,cantidadx,preciox,totalx):

        self.producto=productox
        self.cantidad=cantidadx
        self.precio=preciox
        self.total=totalx


factura1 = Factura('Mouse',5.0,7.0,0.0)

print(factura1.producto,factura1.total)