var Persona = require('../base/Persona.js')

class Estudiante extends Persona { //Herencia (Persona)
    nota_promedio=0.0
    

    //def __init__(this, nombre1, apellido1,nota_promedio1) -> None:
        //super().__init__(nombre1, apellido1)

    constructor(nota_promedio1){
        //super.__init__('','')    
        super('','')    
        this.nota_promedio = nota_promedio1
    }

    mostrarPromedio(){
        console.log('Promedio=',this.nota_promedio)
    }
}

module.exports = Estudiante