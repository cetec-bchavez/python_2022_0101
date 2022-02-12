class Ventas{
    static IVA=0.12

    //@staticmethod
    //#No trabaja NUNCA con variables tipo campo, columna, objetos
    //#Solo trabaja con Variables estaticas o locales
    static GetIva() {
        return Ventas.IVA
    }

    //@staticmethod
    static SetIva(valor){
        Ventas.IVA = valor
    }
}

Ventas.IVA = 0.14

console.log(Ventas.IVA)

console.log(Ventas.GetIva())

Ventas.SetIva(0.20)

console.log(Ventas.GetIva())