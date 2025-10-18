#include <stdio.h>

int SumNNaturalNums(int n) {
    int sum = 0;
    for (int i = 1; i <= n; i++) {
        sum += i;
    }
    return sum;
}

int main() {
    int n;
    printf("Give me a number: ");
    scanf("%d", &n);
    while (n <= 0) {
        printf("Give me a number: ");
        scanf("%d", &n);
    }

    printf("The sum of the first %d numbers is %d\n", n, SumNNaturalNums(n));
    return 0;
}
