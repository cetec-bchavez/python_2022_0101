from base.Persona import Persona
from usos.Estudiante import Estudiante
from usos.Tutor import Tutor

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