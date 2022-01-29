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





