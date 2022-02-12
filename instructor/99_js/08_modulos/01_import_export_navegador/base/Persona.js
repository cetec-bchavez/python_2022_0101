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

export {Persona}