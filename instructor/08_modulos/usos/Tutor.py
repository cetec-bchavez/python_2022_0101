from base.Persona import Persona

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