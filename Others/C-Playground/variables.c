#include <stdio.h>
#include <stdbool.h>

int main(){
    int age = 25; // Variable to store age
    int year = 2025; // Variable to store current year
    printf("Your age is %d years.\n", age);
    printf("The year is %d.\n", year);
    printf("You were born in %d.\n\n", year - age);

    float gpa = 3.8; // Variable to store GPA
    float price = 19.99; // Variable to store price
    printf("Your GPA is %.2f.\n", gpa);
    printf("The price of the item is $%.2f.\n\n", price);

    double pi = 3.141592653589793; // Variable to store Pi
    double e = 2.718281828459045; // Variable to store Euler's number
    printf("The value of Pi is %.15lf.\n", pi);
    printf("The value of Euler's number is %.15lf.\n\n", e);

    char grade = 'A'; // Variable to store grade
    char initial = 'J'; // Variable to store initial
    printf("Your grade is %c.\n", grade);
    printf("Your initial is %c.\n\n", initial);

    char name[] = "John Doe"; // Variable to store name
    char city[] = "New York"; // Variable to store city
    printf("Your name is %s.\n", name);
    printf("You live in %s.\n\n", city);

    //For a boolean, I can put 1 for true and 0 for false
    bool isStudent = true; // Variable to store student status
    bool hasGraduated = false; // Variable to store graduation status
    printf("Are you a student? %s.\n", isStudent ? "Yes" : "No");
    printf("Have you graduated? %s.\n", hasGraduated ? "Yes" : "No");
    return 0;
}
