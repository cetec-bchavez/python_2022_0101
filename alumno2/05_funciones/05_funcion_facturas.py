#variables sin TAB son variables globales
cant=0
price=0
total=0

#Las variables con TAB son variables locales
def put_data():
    global cant,price,total    #con global puedo utilizar variables que tenga fuera de DEF

    cant=int(input("Ingresar cantidad: \n"))
    price= float(input("Ingresar precio: \n"))

def procesing_data():
    global cant,price,total

    total= cant * price

def show_message():
    print("Total: ",total)

put_data()
procesing_data()
show_message()
