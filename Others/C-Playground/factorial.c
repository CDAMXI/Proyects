#include <stdio.h>
#include <math.h>

int factorial(int n){
    if(n < 0){return -1;} // Factorial is not defined for negative numbers
    if(n == 0 || n == 1){return 1;}
    return n * factorial(n - 1);
}

int main() {
    int number = 0;
    printf("Enter a non-negative integer: ");
    scanf("%d", &number);

    while (number < 0){
        printf("Enter a non-negative integer: ");
        scanf("%d", &number);
    }
    

    int result = factorial(number);
    printf("Factorial of %d is %d\n", number, result);
    return 0;
}
