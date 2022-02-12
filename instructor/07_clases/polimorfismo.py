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

    def mostrarPromedio(self):
        print('Promedio=',self.nota_promedio)

class Tutor(Persona): #Herencia (Persona)
    materia_principal=''
    numero_materias=0
    

    #def __init__(self, nombre1, apellido1,nota_promedio1) -> None:
        #super().__init__(nombre1, apellido1)

    def __init__(self,materia_principal1,numero_materias1):
        #super.__init__('','')        
        self.materia_principal = materia_principal1
        self.numero_materias = numero_materias1

    def mostrarMaterias(self):
        print('Materia Principal=',self.materia_principal)
        print('Numero Materias=',self.numero_materias)

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
estudiante1.mostrarPromedio()

print('------------------ TUTOR --------------')

#Uso Constructor
tutor1 = Tutor('',0)

tutor1.nombre='Pedro'
tutor1.apellido='Vinueza'
tutor1.materia_principal='Fisica'
tutor1.numero_materias=5

tutor1.mostrarDatos()
tutor1.mostrarMaterias()

print('------------------ POLIMORFISMO --------------')
# De Hijos a Padre
# Se Generaliza Padre
def mostrarDatosGenerales(persona):
    persona.mostrarDatos()


mostrarDatosGenerales(persona1)
mostrarDatosGenerales(estudiante1)
mostrarDatosGenerales(tutor1)