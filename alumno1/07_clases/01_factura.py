class Factura:  
    producto= ''
    cantidad= 0
    precio=0.0
    total=0.0
    

    def __init__(self,productox,cantidadx,preciox,totalx):
        
        self.producto=productox
        self.cantidad=cantidadx
        self.precio=preciox
        self.total=totalx


facturas= []

factura1=Factura('Mouse',5.0,7.0,0.0)
factura2=Factura('Teclado',5.0,7.0,0.0)

factura1.producto='Mouse Genius'
factura2.producto='Teclado Inx'


facturas.append(factura1)
facturas.append(factura2)

print('------ Datos Factura 1 ------')
print(factura1.producto,factura1.total)

print('------ Datos Factura 2 ------')
print(factura2.producto,factura2.total)

print('------ Datos Facturas Todas ------')

for facturax in facturas:   
    print(facturax.producto, facturax.total)
    