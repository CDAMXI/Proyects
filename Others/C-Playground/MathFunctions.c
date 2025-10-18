#include <stdio.h>
#include <math.h>

int main() {
    int x = 9;
    int square_root = sqrt(x);
    int power = pow(x, 2);
    printf("Square root: %d\n", square_root);
    printf("Power: %d\n", power);

    float x_float = 3.14f;
    float round_value = roundf(x_float); //round to nearest integer
    float ceil_value = ceilf(x_float); //round up to nearest integer
    float floor_value = floorf(x_float); //round down to nearest integer
    printf("Round: %.0f\n", round_value);
    printf("Ceil: %.0f\n", ceil_value);
    printf("Floor: %.0f\n", floor_value);

    int x_double = -3;
    int abs_value = abs(x_double); //absolute value
    printf("Absolute value: %d\n", abs_value);

    float x_log = 2.71828f;
    float log_value = logf(x_log); //natural logarithm
    printf("Natural Log: %.5f\n", log_value);

    float x_rad = 0.5f; //radians
    float sin_value = sinf(x_rad); //sine
    float cos_value = cosf(x_rad); //cosine
    float tan_value = tanf(x_rad); //tangent
    printf("Sine: %.5f\n", sin_value);
    printf("Cosine: %.5f\n", cos_value);
    printf("Tangent: %.5f\n", tan_value);

    return 0;
}
