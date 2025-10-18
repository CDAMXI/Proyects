#include <stdio.h>
#include <math.h>

#define PI 3.14159265358979323846

int main() {
    int radius;
    printf("Enter the radius of the sphere: ");
    scanf("%d", &radius);

    double area = PI * pow(radius, 2);
    double surface_area = 4 * PI * pow(radius, 2);
    double volume = (4.0/3.0) * PI * pow(radius, 3);

    printf("Area of the circle: %.2f\n", area);
    printf("Surface area of the sphere: %.2f\n", surface_area);
    printf("Volume of the sphere: %.2f\n", volume);
    return 0;
}
