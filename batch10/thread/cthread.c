#include <stdio.h>
#include <pthread.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/time.h>

void* loop1(void* arg) {
    int num = *((int*)arg);
    for (int x = 0; x < num; x++) {
        printf("%d loop 1\n", x);
    }
    return NULL;
}

void* loop2(void* arg) {
    int num = *((int*)arg);
    for (int x = 0; x < num; x++) {
        printf("%d loop 2\n", x);
    }
    return NULL;
}

int main() {
    pthread_t t1, t2;
    int count = 100;

    struct timeval start, end;
    gettimeofday(&start, NULL);  // Start timing

    // Create threads
    pthread_create(&t1, NULL, loop1, &count);
    pthread_create(&t2, NULL, loop2, &count);

    // Wait for threads to finish
    pthread_join(t1, NULL);
    pthread_join(t2, NULL);

    gettimeofday(&end, NULL);  // End timing

    // Calculate elapsed time in seconds
    double elapsed = (end.tv_sec - start.tv_sec) + 
                     (end.tv_usec - start.tv_usec) / 1000000.0;

    printf("Execution time: %.4f seconds\n", elapsed);

    return 0;
}
