#include <stdio.h>

int main() {
    int a = 10, b = 2, c = 0; // Integer variables

    c = a + b; // Addition
    printf("Addition: %d + %d = %d\n\n", a, b, c);
    c = a - b; // Subtraction
    printf("Subtraction: %d - %d = %d\n\n", a, b, c);
    c = a * b; // Multiplication
    printf("Multiplication: %d * %d = %d\n\n", a, b, c);
    c = a / b; // Division
    printf("Division: %d / %d = %d\n\n", a, b, c);
    c = a % b; // Modulus
    printf("Modulus: %d %% %d = %d\n", a, b, c);
    return 0; // Indicate that the program ended successfully
}
