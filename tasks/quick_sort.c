#define _CRT_SECURE_NO_WARNINGS
#include <stdlib.h>
#include <stdio.h>


// Null checks

#define NULL_CHECK(type, message)                                \
void nullCheck_##type(type* ptr) {                               \
	if (ptr == NULL) {                                           \
		printf(message);                                         \
		exit(11);                                                \
	}                                                            \
}


NULL_CHECK(void, "Out of memory!");
NULL_CHECK(FILE, "File cannot be opened");


size_t branchfree_lomuto_partition(int* arr, size_t start, size_t end);
size_t classic_lomuto_partition(int* arr, size_t start, size_t end);
size_t hoare_partition(int* arr, size_t start, size_t end);
void swap(int* nums, int ind1, int ind2);


#define QUICK_SORT(partition)                        \
void quick_sort_##partition(int* arr, size_t start, size_t end) {       \
    if (end <= start) return 0;                                         \
    if (end == start + 1) {                                             \
        if (arr[start] > arr[end]) swap(arr, start, end);               \
        return 0;                                                       \
    }                                                                   \
    if (start < end) {                                                  \
        size_t pivot = ##partition(arr, start, end);                    \
        quick_sort_##partition(arr, start, pivot);                      \
        quick_sort_##partition(arr, pivot + 1, end);                    \
    }                                                                   \
}                                                                       \

QUICK_SORT(hoare_partition);
QUICK_SORT(classic_lomuto_partition);
QUICK_SORT(branchfree_lomuto_partition);


void rand_array(int* arr, int len) {
    srand(time(NULL));
    for (size_t i = 0; i < len; i++) {
        int r = rand() % 100;
        arr[i] = r;
    }
}


void printArr(int* arr, size_t len) {
    for (size_t i = 0; i < len;i++) {
        printf("%d ", arr[i]);
    }
}


void swap(int* nums, int ind1, int ind2) {

    int tmp;
    tmp = nums[ind1];
    nums[ind1] = nums[ind2];
    nums[ind2] = tmp;
}


size_t hoare_partition(int* arr, size_t start, size_t end) {

    size_t pivot_index = start + (rand() % (end - start));
    if (pivot_index != start) {
        swap(arr, pivot_index, start);
    }

    int pivot_value = arr[start];
    size_t i = start + 1;
    size_t j = end - 1;

    while (1) {
        while (arr[i] < pivot_value) {
            i++;
        }
        while (arr[j] > pivot_value) {
            j--;
        }
        if (i >= j) break;
        swap(arr, i++, j--);
    }
    swap(arr, start, j);
    return j;


}

size_t branchfree_lomuto_partition(int* arr, size_t start, size_t end) {

    size_t pivot_index = start;
    int pivot_value = arr[start];
    
    do {
        start++;
    } while (arr[start] < pivot_value && start <= end);

    for (size_t i = start; i < end; i++) {
        int tmp = arr[i];
        int smaller = - (int) (tmp < pivot_value);
        int delta = smaller & (i - start);

        arr[start + delta] = arr[start];
        arr[i - delta] = tmp;
        start -= smaller;
    }

    start--;
    arr[pivot_index] = arr[start];
    arr[start] = pivot_value;
    return start;


}

size_t classic_lomuto_partition(int* arr, size_t start, size_t end) {


    size_t pivot_index = start + (rand() % (end - start));
    if (pivot_index != start) {
        swap(arr, pivot_index, start);
    }

    int pivot_value = arr[start];
    size_t i = start;

    for (size_t j = start ; j < end; j++) {
        if (arr[j] < pivot_value) {
            i++;
            swap(arr, i, j);
        }
    }
    swap(arr, i, start);
    return i;
}


 
int main() {

    size_t len = 1003;
    int* array = (int*)malloc(len * sizeof(int));

    nullCheck_void(array);

    rand_array(array, len);
    
    quick_sort_hoare_partition(array, 0, len - 1);

    printArr(array, len);
    free(array);
}
