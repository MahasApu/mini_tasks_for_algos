#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <stdlib.h>
#include <malloc.h>
#include <string.h>
#include <math.h>
#include <stdbool.h>


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



// Initialization of structs

#define DYN_ARR(type, dynArrForStruct, name_of, format_code)    \
typedef struct {                                                \
   type* data;                                                  \
   size_t len;                                                  \
   size_t capacity;                                             \
} dynArrForStruct;                                              \
                                                                \
void init_##dynArrForStruct(dynArrForStruct* arr) {             \
   arr->data = NULL;                                            \
   arr->len = 0;                                                \
   arr->capacity = 1;                                           \
}                                                               \
																								  \
void add_##name_of(dynArrForStruct* arr, type elem) {                                             \
                                                                                                  \
	if (arr->capacity <= arr->len) {                                                              \
		arr->capacity = arr->capacity * 2;                                                        \
		arr->data = (type*)realloc(arr->data,  arr->capacity * sizeof(type));                     \
		printf("arr cap %zu len %zu \n", arr->capacity, arr->len); \
		nullCheck_void(arr->data);                                                                \
	}                                                                                             \
	if (arr->data == NULL) {                                                                      \
		arr->data = (type*)malloc(arr->capacity * sizeof(type));                                  \
		nullCheck_void(arr->data);                                                                \
	}                                                                                             \
	arr->data[arr->len++] = elem;                                                                 \
}                                                                                                 \
void del_##name_of(dynArrForStruct* arr) {                                                        \
	arr->len -= 1;                                                                                \
	if (arr->len <= (arr->capacity / 4)) {                                                        \
		arr->capacity = arr->capacity / 2;                                                        \
		arr->data = (type*)realloc(arr->data, arr->capacity * sizeof(type));                      \
		nullCheck_void(arr->data);                                                                \
	}                                                                                             \
}                                                                                                 \
type get_##name_of(dynArrForStruct* arr, size_t index) {                                          \
	if (index >= arr->len) {                                                                      \
		printf("Error: index out of range (index: %zu, len: %zu)\n", index, arr->len);            \
		exit(1);                                                                                  \
	}                                                                                             \
	return arr->data[index];                                                                      \
}                                                                                                 \
void free_##dynArrForStruct(dynArrForStruct* arr){                                                \
	free(arr->data);                                                                              \
	arr->capacity = 0;                                                                            \
	arr->len = 0;                                                                                 \
}                                                                                                 \
void printArr(dynArrForStruct* arr) {                                                             \
	for (size_t i = 0; i < arr->len; i++) {                                                       \
		printf(format_code , arr->data[i]);                                                       \
	}                                                                                             \
}

DYN_ARR(int, DynArrInt, element, "%d ");



int main() {
	DynArrInt array;
	init_DynArrInt(&array);
	int len1 = 12;

	for (int i = 0; i < len1; i++) {
		add_element(&array, rand() % 100);
	}
	printArr(&array);
	printf("\n%d",get_element(&array, 4));
	for (int i = 0; i < 9; i++) {
		del_element(&array);
		printf("\nlen %zu, cap %zu", array.len, array.capacity);
	}
	free_DynArrInt(&array);

}