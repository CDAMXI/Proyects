#include <stdio.h>

int doubleFactorial(int n){
    if (n == 0 || n == 1)
        return 1;
    else
        return n * doubleFactorial(n - 2);
}

int main(){
    int n;
    printf("Enter a number: ");
    scanf("%d", &n);
    printf("The double factorial of %d is %d\n", n, doubleFactorial(n));
    return 0;
}
