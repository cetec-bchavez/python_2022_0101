class Ventas:
    IVA=0.12

    @staticmethod
    #No trabaja NUNCA con variables tipo campo, columna, objetos
    #Solo trabaja con Variables estaticas o locales
    def GetIva():        
        return Ventas.IVA

    @staticmethod
    def SetIva(valor):
        Ventas.IVA = valor


Ventas.IVA = 0.14

print(Ventas.IVA)

print(Ventas.GetIva())

Ventas.SetIva(0.20)

print(Ventas.GetIva())