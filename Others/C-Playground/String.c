#include <stdio.h>
#include <string.h>

int main(){
    char noun[50] = "";
    char verb[50] = "";
    char adjective1[50] = "";
    char adjective2[50] = "";
    char adjective3[50] = "";

    printf("Enter an adjective (description): ");
    fgets(adjective1, sizeof(adjective1), stdin);
    adjective1[strlen(adjective1) - 1] = '\0'; // Remove newline character

    printf("Enter an noun (animal or person): ");
    fgets(noun, sizeof(noun), stdin);
    noun[strlen(noun) - 1] = '\0'; // Remove newline character
    
    printf("Enter an adjective (description): ");
    fgets(adjective2, sizeof(adjective2), stdin);
    adjective2[strlen(adjective2) - 1] = '\0'; // Remove newline character
    
    printf("Enter an verb (ending w/ -ing): ");
    fgets(verb, sizeof(verb), stdin);
    verb[strlen(verb) - 1] = '\0'; // Remove newline character
    
    printf("Enter an adjective (description): ");
    fgets(adjective3, sizeof(adjective3), stdin);
    adjective3[strlen(adjective3) - 1] = '\0'; // Remove newline character

    printf("\nHere is your story:\n");
    printf("Once upon a time, there was a %s %s.\n", adjective1, noun);
    printf("Every day, it would go %s in the %s forest.\n", verb, adjective2);
    printf("One day, it met a %s friend and they lived happily ever after!\n", adjective3);
    return 0;
}
