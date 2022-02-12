class Persona:
    nombre=''
    apellido=''

    def __init__(self,nombre1,apellido1) -> None:        
        self.nombre=nombre1
        self.apellido=apellido1 

    def mostrarDatos(self):
        print(self.nombre,self.apellido)


class Estudiante(Persona): #Herencia (Persona)
    nota_promedio=0.0
    

    #def __init__(self, nombre1, apellido1,nota_promedio1) -> None:
        #super().__init__(nombre1, apellido1)

    def __init__(self,nota_promedio1):
        #super.__init__('','')        
        self.nota_promedio = nota_promedio1

    def mostrarDatos(self):
        print(self.nombre,self.apellido)
        print('Promedio=',self.nota_promedio)

print('------------------ PERSONA --------------')
#Uso Constructor
persona1 = Persona('Luis','Perez')

persona1.mostrarDatos()

print('------------------ ESTUDIANTE --------------')

#Uso Constructor
estudiante1 = Estudiante(0.0)

estudiante1.nombre='Veronica'
estudiante1.apellido='sanchez'
estudiante1.nota_promedio=5.4

estudiante1.mostrarDatos()