#include <stdio.h>
#include <math.h>

int fibonacci(int n){
    if(n <= 0){return 0;}
    if(n == 1){return 1;}
    return fibonacci(n - 1) + fibonacci(n - 2);
}

int main() {
    int number = 0;
    printf("Enter a non-negative integer: ");
    scanf("%d", &number);

    while (number < 0){
        printf("Enter a non-negative integer: ");
        scanf("%d", &number);
    }

    int result = fibonacci(number);
    printf("Fibonacci of %d is %d\n", number, result);
    return 0;
}
