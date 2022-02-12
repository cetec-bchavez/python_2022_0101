function factorial(numero) {

    if(numero==1) {
        return 1
    } else {
        console.log(numero)
        return numero * factorial(numero-1)
    }
}

//5= 5*4*3*2*1=120
let resultado = factorial(5)

console.log(resultado)