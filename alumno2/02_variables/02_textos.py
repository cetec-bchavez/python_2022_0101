titulo="centro de salud"

titulo=titulo.upper()

print(titulo)
#diferentes formas de hacer lo mismo
print("centro de salud".upper())

#cambiar una o varias palabras de un texto previamente guardado

print(titulo.replace("centro","patio"))
#solo cambia el centro dando= patio de salud     (solo una vez) y luego vuelve a ser "centro de salud"

#separar cada palabra con un termino que definiremos

#var.split(" oda ")

#dando     centro, oda de, oda salud

pato="patito patudo pelon"
print(titulo.replace(" "," f "))     #cambiar terminos con otros

nombres="Pedro,Pablo,Pancho"

for panchito in nombres:                  #panchito es una variable temporal
    print("nombres +",panchito)           #aqui hay 17 terminos

print("cambio")

nombresito=nombres.split(",")       #split separa los terminos de "pedro,pablo,pancho"  a  "pedro" "pablo" "pancho"

for panchit in nombresito:         #aqui hay 3 terminos luego se separar con split
    print("nombres +",panchit)


print("ejercicio nombre completo")
nombres2="pedro ramiro,pablo alonzo,jose mendoza"
nombresito2=nombres2.split(",")                     #separa todos los terminos en 3 terminos

for var in nombresito2:               #for VARIABLEtemporal in VARIABLEquealmacenadatos
    print("nombre" + var)             #imprime los 3 terminos anteriores
    nombre=var.split(" ")[0]          #separa el nombre del apellido y guarda en NOMBRE el termino antes del espacio
    apellido=var.split(" ")[1]        #separa el nombre del apellido y guarda en NOMBRE el termino despues del espacio
    
    print("nombre + ", nombre)
    print("apellido + ", apellido)






