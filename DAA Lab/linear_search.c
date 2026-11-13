//Write a program to execute linear search and observe how it grows calculate the complexity
#include <stdio.h>
int linear_search(int arr[],int n, int key){
    for(int i = 0; i < n; i++){
        if(arr[i] == key){
            return i;
        }
    }
    return -1;
}

int main(){
    int arr[] = {10, 25, 3, 47, 8, 99};
    int n = 6;
    int key = 47;
    int result = linear_search(arr, n, key);

    if (result == -1)
        printf("Element not found\n");
    else
        printf("Element %d found at index %d\n", key, result);

    return 0;
}