#include <stdio.h>

int main(){
    int age = 21;
    float price = 19.99;
    double pi = 3.141592653589793;
    char currency = '$';
    char name[] = "Charlie";

    printf("Age: %d years\n", age);
    printf("Price: %.2f %c\n", price, currency);
    printf("Value of Pi: %.15lf\n", pi);
    printf("Name: %s\n\n", name);

    int num1 = 1, num2 = 10, num3 = 100;
    printf("Numbers: %3d\n",num1);
    printf("Numbers: %3d\n",num2);
    printf("Numbers: %3d\n\n",num3);

    return 0;
}
