#include <stdio.h>

int main() {
    int size;
    printf("Enter the size of array: ");
    scanf("%d", &size);

    int arr[size];

    printf("\nRandomly generated arrya:")
    for(int i = 0; i<size; i++) {
        arr[i] = rand() % 100;
        printf("%d ", arr[i]);
    }
    printf("\n");

    int smallest = arr[0], secondSmallest = arr[0];
    int largest = arr[0], secondLargest = arr[0];
    for(int i = 0; i<size; i++) {
        int num = arr[i];
        if (num < smallest) {
            secondSmallest = smallest;
            smallest = num;
        } else if (num < secondSmallest && num != smallest) {
            secondSmallest = num;
        }
        if (num > largest) {
            secondLargest = largest;
            largest = num;
        } else if (num > secondLargest && num != largest) {
            secondLargest = num;
        }    
    }
