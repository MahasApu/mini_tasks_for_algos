import random
from typing import List


def swap(array: List[int], ind1: int, ind2: int):
    temp = array[ind1]
    array[ind1] = array[ind2]
    array[ind2] = temp



# kind of partition idea of quick sort
def sortColors(nums: List[int]):
    zeros = 0
    twos = len(nums) - 1

    curr_number = 0

    while True:

        if curr_number > twos:
            break

        if nums[curr_number] == 0:
            swap(nums, zeros, curr_number)
            curr_number += 1
            zeros += 1

        elif nums[curr_number] == 1:
            curr_number += 1

        # not to take a step since there is a need to check the swapped number (0 1 2)
        else:
            swap(nums, twos, curr_number)
            twos -= 1


def generate_rand_arr(size: int) -> List[int]:
    return [random.randint(0, 2) for __ in range(size)]


if __name__ == '__main__':
    arr = generate_rand_arr(10)
    # sort_tester(arr, hoare_partition)
    sortColors(arr)
    print(arr)
