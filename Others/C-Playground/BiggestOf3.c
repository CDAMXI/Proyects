#include <stdio.h>
#include <stdlib.h>

static int cmp_int_asc(const void *a, const void *b) {
    int ia = *(const int*)a;
    int ib = *(const int*)b;
    return (ia > ib) - (ia < ib);
}

int BiggestOf3(int nums[3]){
    qsort(nums, 3, sizeof(int), cmp_int_asc);
    return nums[2];
}

int main(){
    int nums[3];
    for (int i = 0; i < 3; i++) {
        printf("Introduce a value: ");
        scanf("%d", &nums[i]);
    }

    printf("The biggest number among %d, %d and %d is %d.\n",
           nums[0], nums[1], nums[2], BiggestOf3(nums));

    return 0;
}
