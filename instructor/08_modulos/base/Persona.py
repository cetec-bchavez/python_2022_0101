class Persona:
    nombre=''
    apellido=''

    def __init__(self,nombre1,apellido1) -> None:        
        self.nombre=nombre1
        self.apellido=apellido1 

    def mostrarDatos(self):
        print(self.nombre,self.apellido)