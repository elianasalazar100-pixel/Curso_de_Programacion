// ejercicio 1 // 

#include <iostream>
using namespace std;

int main() {
    cout << "¡Hola, Mundo!" << endl;

    int Miedad = 25;
    float fecha = 19.12;
    char caracter = 'E';
    bool valorBooleano = true;

    cout << "Tengo: " << Miedad << endl;
    cout << "Fecha de nacimiento: " << fecha << endl;
    cout << "Mi inicial: " << caracter << endl;
    cout << "Valor del booleano: " << valorBooleano << endl;

    return 0;
}

// ejercicio 2 //

#include <iostream> 
#include <cmath>    

int main() {
    double num1, num2;

    cout << "Introduce el primer numero: ";
    cin >> num1;
    cout << "Introduce el segundo numero: ";
    cin >> num2;
    
    
    cout << "Suma: " << num1 + num2 << endl;
    cout << "Resta: " << num1 - num2 << endl;
    cout << "Multiplicacion: " << num1 * num2 << endl;
    
    if (num2 != 0) {
        cout << "Division: " << num1 / num2 << endl;
    } else {
        cout << "No se puede dividir por cero." << endl;
    }

    
    cout << "Potencia (" << num1 << " elevado a " << num2 << "): " << pow(num1, num2) << endl;
    

    if (num1 >= 0) {
        cout << "Raiz cuadrada de " << num1 << ": " << sqrt(num1) << endl;
    } else {
        cout << "Raiz cuadrada de " << num1 << ": No se puede calcular la raiz de un numero negativo." << endl;
    }

    return 0;
}

// ejercicio 3 // 

#include <iostream>

int main() {
    int edad;

    
    cout << "Por favor, introduce tu edad: ";
    cin >> edad;

    
    if (edad >= 18) {
        cout << "Eres mayor de edad." << endl;
    } else {
        cout << "Eres menor de edad." << endl;
    }

    return 0;
}

// ejercicio 4 //

#include <iostream>

#define LIMITE 10

int main() {
    int numero;

    
     << "Introduce un numero para ver su tabla de multiplicar: ";
     >> numero;
    

    cout << "Tabla de multiplicar del " << numero << ":" << endl;

    
    for (int i = 1; i <= LIMITE; ++i) {
        cout << numero << " x " << i << " = " << (numero * i) << endl;
    }

    return 0;
}

// ejercicio 5


#include <iostream>

int main() {
    int numeroSecreto = 71;
    int intentos = 0;

    cout << "¡Adivina el numero secreto: " << endl;

    while (intentos != numeroSecreto) {
        cout << "Introduce un numero: ";
        cin >> intentos;

        if (intentos < numeroSecreto) {
            cout << "El numero secreto es mas alto." << endl;
        } else if (intentos > numeroSecreto) {
            cout << "El numero secreto es mas bajo." << endl;
        }
    }

    cout << "¡Felicidades! Adivinaste el numero secreto: " << numeroSecreto << endl;

    return 0;
}

// ejercicio 6

#include <iostream>

int main() {
    int opcion;

    do {
        
        cout << "1. Saludar" << endl;
        cout << "2. Despedirse" << endl;
        cout << "3. Salir" << endl;
        cout << "Elige una opcion: ";
        cin >> opcion;

        switch (opcion) {
            case 1:
                cout << "¡Hola para ti tambien!" << endl;
                break;
            case 2:
                cout << "¡Adios!." << endl;
                break;
            case 3:
                cout << "Saliendo..." << endl;
                break;
            default: 
                cout << "Opcion no valida." << endl;
                break;
        }

    } while (opcion != 3);

    return 0;
}
