//implement array of N integers find smallest, largest, second smallest and second largest numbers in the array
#include <stdio.h>
#define N 15

int main() {
    int arr[N];
    int i, smallest, largest, second_smallest, second_largest;

    // Input the array elements
    printf("Enter %d integers:\n", N);
    for (i = 0; i < N; i++) {
        scanf("%d", &arr[i]);
    }

    // Initialize variables
    smallest = arr[0];
    largest = arr[0];
    second_smallest = arr[0];
    second_largest = arr[0];

    // Find smallest and largest
    for (i = 1; i < N; i++) {
        if (arr[i] < smallest) {
            smallest = arr[i];
        }
        if (arr[i] > largest) {
            largest = arr[i];
        }
    }

    // Find second smallest and second largest
    for (i = 0; i < N; i++) {
        if (arr[i] > second_largest && arr[i] < largest) {
            second_largest = arr[i];
        }
        if (arr[i] < second_smallest && arr[i] > smallest) {
            second_smallest = arr[i];
        }
    }

    // Output the results
    printf("Smallest number: %d\n", smallest);
    printf("Largest number: %d\n", largest);
    printf("Second smallest number: %d\n", second_smallest);
    printf("Second largest number: %d\n", second_largest);

    return 0;
}
