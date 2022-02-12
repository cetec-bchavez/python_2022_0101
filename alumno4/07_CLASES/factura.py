class Factura:
    #Variables Columnas, Variables Complejas
    producto=''
    cantidad=0
    precio=0.0
    total=0.0

    #Mecanico, PRIMEROS VALORES Ejm. Factura('Mouse',5.0,7.0,0.0)
    #Constructor (Fila de Datos)
    def __init__(self,productox,cantidadx,preciox,totalx):

        self.producto=productox
        self.cantidad=cantidadx
        self.precio=preciox
        self.total=totalx

    #self (Hace referencia a variables de la clase, columnas, objetos)
    #self (Hace referencia a metodos/funciones de la clase, columnas, objetos)
    def calcular_total(self):
        self.total = self.cantidad * self.precio


# Hoja Calculo completa (columnas, y filas de datos)
facturas=[] 
# OBJETO (Fila de Datos)
# nombre = Clase(Valor1,Valor2,Valor3)
#Factura 1 (Fila Datos 1)
#Uso Constructor
factura1 = Factura('Mouse',5.0,7.0,0.0) # Fila factura1

factura1.producto='Mouse Genius' # Apuntamos a una Celda (producto) de fila factura1
factura1.calcular_total()
facturas.append(factura1)

print('------------- Datos Factura 1 --------------')
print(factura1.producto,factura1.total)

#Factura 2 (Fila Datos 2)
#Uso Constructor
factura2 = Factura('Teclado',7.0,6.0,0.0) # Fila factura2
#Columnas se cambian a Celdas
factura2.producto='Teclado Inx' # Apuntamos a una Celda (producto) de fila factura2
factura2.calcular_total()

facturas.append(factura2)

print('------------- Datos Factura 2 --------------')
print(factura2.producto,factura2.total)


print('------------- Datos Facturas TODOS --------------')

for facturax in facturas: 
    print(facturax.producto,facturax.total)
    #print(facturax)