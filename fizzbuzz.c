
#include <stdio.h>
#include <time.h>

int main() {
    clock_t start, end;
    double cpu_time_used;
    
    start = clock(); // Start the clock
    
    for (int i = 1; i <= 200000; i++) {
        if (i % 15 == 0) {
            printf("FizzBuzz\n");
        } else if (i % 3 == 0) {
            printf("Fizz\n");
        } else if (i % 5 == 0) {
            printf("Buzz\n");
        } else {
            printf("%d\n", i);
        }
    }
    
    end = clock(); // End the clock
    cpu_time_used = ((double)(end - start)) / CLOCKS_PER_SEC; // Calculate execution time
    
    printf("Execution Time: %f seconds\n", cpu_time_used); // Print execution time
    
    return 0;
}
