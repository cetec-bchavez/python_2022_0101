class Persona {
    nombre=''
    apellido=''

    constructor(nombre1,apellido1) {        
        this.nombre=nombre1
        this.apellido=apellido1 
    }

    mostrarDatos() {
        console.log(this.nombre,this.apellido)
    }
}

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