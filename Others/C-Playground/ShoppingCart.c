#include <stdio.h>
#include <string.h>

int main(){
    char items[50] = "";
    float price = 0.0f;
    int quantity = 0;
    char currency = '$'; // Default currency symbol
    float total = 0.0f;

    printf("Enter item name: ");
    fgets(items, sizeof(items), stdin); // allows spaces
    items[strcspn(items, "\n")] = '\0'; // remove trailing newline

    printf("Enter price of each item: ");
    scanf("%f", &price);

    printf("Enter quantity: ");
    scanf("%d", &quantity);

    total = price * quantity;

    printf("\n--- Shopping Cart ---\n");
    printf("Item: %s\n", items);
    printf("Price per item: %.2f %c\n", price, currency);
    printf("Quantity: %d\n", quantity);
    printf("Total cost: %.2f %c\n", total, currency);

    return 0;
}
