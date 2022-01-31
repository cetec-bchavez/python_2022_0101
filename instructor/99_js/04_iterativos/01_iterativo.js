let y=0

for(let x=5;x<=50;x+=5) {
    y = 5*x + 30

    console.log(`x=${x},  y=${y}`)
}

console.log('------------------- 2da Forma ---------------')

for(x of [5,10,15,20,25,30,35,40,45,50]) {
    y = 5*x + 30

    console.log(`x=${x},  y=${y}`)
}

document.write('<h1 style="color:white;background-color:blue">Fin Iterativos</h1>')

console.log('------------------- 2da Forma Formato Html ---------------')

document.write('<ol>')

for(x of [5,10,15,20,25,30,35,40,45,50]) {
    y = 5*x + 30

    document.write(`<li> x=${x},  y=${y} </li>`)
}

document.write('</ol>')