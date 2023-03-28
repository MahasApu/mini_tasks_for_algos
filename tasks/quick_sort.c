
#define _CRT_SECURE_NO_WARNINGS
#include <stdlib.h>
#include <stdio.h>
#include <time.h>
#include <assert.h>


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


int branchfree_lomuto_partition(int* arr, int start, int end);
int classic_lomuto_partition(int* arr, int start, int end);
int hoare_partition(int* arr, int start, int end);
void swap(int* nums, int ind1, int ind2);


#define QUICK_SORT(partition)                                           \
void quick_sort_##partition(int* arr, int start, int end) {             \
    if (start < end) {                                                  \
        int pivot = ##partition(arr, start, end);                       \
        quick_sort_##partition(arr, start, pivot - 1);                  \
        quick_sort_##partition(arr, pivot + 1, end);                    \
    }                                                                   \
}                                                                       \

QUICK_SORT(hoare_partition);
QUICK_SORT(classic_lomuto_partition);
QUICK_SORT(branchfree_lomuto_partition);


void rand_array(int* arr, int len) {
    srand(time(NULL));
    for (int i = 0; i < len; i++) {
        int r = rand() % 100;
        arr[i] = r;
    }
}


void printArr(int* arr, int len) {
    for (int i = 0; i < len;i++) {
        printf("%d ", arr[i]);
    }
}


void swap(int* ind1, int* ind2) {

    int tmp = *ind1;
    *ind1 = *ind2;
    *ind2 = tmp;
}




int hoare_partition(int* arr, int start, int end) {

    int pivot_index = start + (rand() % (end - start));
    if (pivot_index != start) {
        swap(&arr[pivot_index], &arr[start]);
    }

    int pivot_value = arr[start];
    int i = start + 1;
    int j = end;

    while (1) {
        while (arr[i] < pivot_value) {
            i++;
        }
        while (arr[j] > pivot_value) {
            j--;
        }
        if (i >= j) break;
        swap(&arr[i++], &arr[j--]);
    }
    swap(&arr[start], &arr[j]);
    return j;
}





int branchfree_lomuto_partition(int* arr, int start, int end) {

    if (end  <= start) {
        return start;
    }
    else if (end - start < 2) {
        return start;
    }

    if (arr[start] > arr[end]) {
        swap(&arr[start], &arr[end]);
    }


    int pivot_index = start;
    int pivot_value = arr[start];

    do {
        start++;

    } while (arr[start] < pivot_value);

    for (int i = start + 1; i < end; i++) {

        int tmp = arr[i];
        int smaller = -(int)(tmp < pivot_value);
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

int classic_lomuto_partition(int* arr, int start, int end) {

    if (end - start <= 0) {
        return start;
    }
    if (end - start == 1) {
        if (arr[start] > arr[end]) {
            swap(&arr[start], &arr[end]);
        }
        return start;
    }

    int pivot_index = start + rand() % (end - start);
    swap(&arr[pivot_index], &arr[start]);

    int pivot_value = arr[start];
    int j = start;

    for (int i = start + 1; i <= end; i++) {
        if (arr[i] < pivot_value) {
            j++;
            swap(&arr[i], &arr[j]);
        }

        else if (arr[i] == arr[start]) {
            if (rand() % 3 == 0) {
                j++;
                swap(&arr[i], &arr[j]);
            }
        }
    }
    swap(&arr[j], &arr[start]);

    return j;
}


int main() {

    int len = 10000000;
    int* array1 = (int*)malloc(len * sizeof(int));
    nullCheck_void(array1);
    rand_array(array1, len);

    int* array2 = (int*)malloc(len * sizeof(int));
    nullCheck_void(array2);


    for (size_t i = 0; i < len; i++) {
        array2[i] = array1[i];
    }

    FILE* output_file = fopen("output.txt", "w+");
    nullCheck_FILE(output_file);

    size_t times = 5;

    /* for Hoare partition */
    for (size_t i = 0; i < times; i++) {

        clock_t start = clock();
        quick_sort_hoare_partition(array1, 0, len - 1);
        clock_t end = clock();
        double spent_time = (double)(end - start) / CLOCKS_PER_SEC;

        fprintf(output_file, "%f ", spent_time);
    }


    fprintf(output_file, "\n");

    /* for classic Lomuto partition */
    for (size_t i = 0; i < times; i++) {

        clock_t start = clock();
        quick_sort_classic_lomuto_partition(array2, 0, len - 1);
        clock_t end = clock();
        double spent_time = (double)(end - start) / CLOCKS_PER_SEC;

        fprintf(output_file, "%f ", spent_time);
    }

    fprintf(output_file, "\n");


    //
    ///* for branch-free Lomuto partition */
    //for (size_t i = 0; i < times; i++) {

    //    clock_t start = clock();
    //    quick_sort_branchfree_lomuto_partition(array1, 0, len - 1);
    //    clock_t end = clock();
    //    double spent_time = (double)(end - start) / CLOCKS_PER_SEC;

    //    fprintf(output_file, "%f ", spent_time);
    //}



    fclose(output_file);
    // printArr(array, len);
    free(array1);
    free(array2);
}
