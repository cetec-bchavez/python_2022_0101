def factorial(numero):

    if numero==1:
        return 1
    else:
        print(numero)
        return numero * factorial(numero-1)

#5= 5*4*3*2*1=120
resultado = factorial(5)

print(resultado)