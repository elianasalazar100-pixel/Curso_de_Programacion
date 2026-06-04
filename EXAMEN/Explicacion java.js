
let nombreUsuario = "fleursole";
console.log("Nombre de usuario inicial:", nombreUsuario);
console.log(`Nombre de usuario actual: ${nombreUsuario}`);


let edad = 18;
let enunciado = Number(prompt("Por favor, ingresa tu edad:"));

if (enunciado >= 18) {
    console.log ("Acceso concedido, cumple la edad.");
}
else if (enunciado <= 18) {
    console.log ("Acceso denegado, edad no valida.");
}


const rolUsuario = "ADMIN";

console.log(`el nivel del usuario es: ${rolUsuario}.`);

switch (rolUsuario) {
    case "ADMIN":
        console.log("acceso concedido.");
        break;
    default:
        console.log("acceso denegado."); } 



let numero = 1;
let objetivo = 10;

const numero = 1;
console.log(`Tabla de Sumar del ${numero}`);

for (let i = 1; i <= 10; i++) {
    const resultado = numero + i;
    console.log(`${numero} + ${i} = ${resultado}`);
}

while (numero < objetivo) {
    const resultado += 1;
    console.log(resultado);
    if (objetivo == resultado) {
        break;
    }
}

let nombre = promp("como te llamas?");
console.log("tu nombre es:", nombre);
console.log("tipo de dato:", typeof nombre);

let edad = number(prompt("cuantos años tienes?"));
console.log("tu edad es:", edad);
console.log ("tipo de dato:", typeof edad);
