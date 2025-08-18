#include <stdio.h>
#include <time.h>

void loop1(int num) {
    for (int x = 0; x < num; x++) {
        printf("%d loop 1\n", x);
    }
}

void loop2(int num) {
    for (int x = 0; x < num; x++) {
        printf("%d loop 2\n", x);
    }
}

int main() {
    clock_t start_time, end_time;
    double time_taken;

    start_time = clock(); // Start time

    loop1(10000);
    loop2(10000);

    end_time = clock(); // End time

    time_taken = ((double)(end_time - start_time)) / CLOCKS_PER_SEC;

    printf("Program executed in %.2f seconds\n", time_taken);

    return 0;
}
