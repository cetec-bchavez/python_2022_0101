#tipando codigo
#tipar es citar explicitamente de que tipo es el codigo

from pickle import TRUE


nombre="pablito" #str, str()
edad=28
verdades=True

nombre:str="pablito"       #en este citamos el tipo de variable
edad:int=28                #entero
verdades:bool=True         #booleano, verdadero o falso

venta=20.5     #float osea decimal

venta=int(venta) #al transformar un decimal(float) a un entero(int) este se redondea

print(venta)
#pasa de float a int (de 20.5 a 20)

#las constantes solo se declaran de preferencia en mayuscula
IVA=0.12

