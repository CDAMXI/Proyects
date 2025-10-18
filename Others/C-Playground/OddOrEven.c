#include <stdio.h>
#include <string.h>

const char* OddOrEven(int n){
    if(n % 2 == 0){return "Even";}
    return "Odd";
}

int main(){
    int n;
    printf("Give me a number: ");
    scanf("%d", &n);
    while (n < 0)
    {
        printf("Give me a number: ");
        scanf("%d", &n);
    }

    if (strcmp(OddOrEven(n), "Even") == 0){
        printf("%d is an even number\n", n);
    }
    else {
        printf("%d is an odd number\n", n);
    }
    
    return 0;
}
