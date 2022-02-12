from base.Persona import Persona

class Estudiante(Persona): #Herencia (Persona)
    nota_promedio=0.0
    

    #def __init__(self, nombre1, apellido1,nota_promedio1) -> None:
        #super().__init__(nombre1, apellido1)

    def __init__(self,nota_promedio1):
        #super.__init__('','')        
        self.nota_promedio = nota_promedio1

    def mostrarPromedio(self):
        print('Promedio=',self.nota_promedio)