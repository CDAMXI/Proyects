#include <stdio.h>
#include <string.h>

int main(){
    int age = 0;
    float gpa = 0.0f;
    char grade = '\0'; // Single quotes for single characters
    char name[30] = ""; // Max length of the string

    printf("Enter your age: ");
    scanf("%d", &age); 

    printf("Enter your gpa: ");
    scanf("%f", &gpa); // sin .2 aquí

    printf("Enter your grade: ");
    scanf(" %c", &grade); // espacio antes de %c para evitar leer \n

    getchar(); // consume el salto de línea pendiente si lo hubiera

    printf("Enter your name: ");
    fgets(name, sizeof(name), stdin); // permite espacios

    // Mostramos los datos para comprobar
    printf("\n--- Results ---\n");
    printf("Age: %d\n", age);
    printf("GPA: %.2f\n", gpa); // aquí sí usamos .2 para mostrar
    printf("Grade: %c\n", grade);
    printf("Name: %s\n", name);

    return 0;
}
