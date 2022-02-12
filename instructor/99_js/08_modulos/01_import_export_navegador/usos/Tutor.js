import {Persona} from '../base/Persona.js'

class Tutor extends Persona { //Herencia (Persona)
    materia_principal=''
    numero_materias=0
    

    //def __init__(this, nombre1, apellido1,nota_promedio1) -> None:
        //super().__init__(nombre1, apellido1)

    constructor(materia_principal1,numero_materias1){
        //super.__init__('','')    
        super('','')    
        this.materia_principal = materia_principal1
        this.numero_materias = numero_materias1
    }

    mostrarMaterias(){
        console.log('Materia Principal=',this.materia_principal)
        console.log('Numero Materias=',this.numero_materias)
    }
}

export {Tutor}