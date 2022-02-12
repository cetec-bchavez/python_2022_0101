import {Persona} from './base/Persona.js'
import {Estudiante} from './usos/Estudiante.js'
import {Tutor} from './usos/Tutor.js'

class Principal { 

    static procesar() {

        console.log('------------------ PERSONA --------------')
        //Uso Constructor
        let persona1 = new Persona('Luis','Perez')

        persona1.mostrarDatos()

        console.log('------------------ ESTUDIANTE --------------')

        //Uso Constructor
        let estudiante1 = new Estudiante(0.0)

        estudiante1.nombre='Veronica'
        estudiante1.apellido='sanchez'
        estudiante1.nota_promedio=5.4

        estudiante1.mostrarDatos()
        estudiante1.mostrarPromedio()

        console.log('------------------ TUTOR --------------')

        //Uso Constructor
        let tutor1 = new Tutor('',0)

        tutor1.nombre='Pedro'
        tutor1.apellido='Vinueza'
        tutor1.materia_principal='Fisica'
        tutor1.numero_materias=5

        tutor1.mostrarDatos()
        tutor1.mostrarMaterias()

        console.log('------------------ POLIMORFISMO --------------')
        // De Hijos a Padre
        // Se Generaliza Padre
        function mostrarDatosGenerales(persona) {
            persona.mostrarDatos()
        }


        mostrarDatosGenerales(persona1)
        mostrarDatosGenerales(estudiante1)
        mostrarDatosGenerales(tutor1)
    }
}

Principal.procesar()