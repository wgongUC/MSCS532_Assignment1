# Name: Weevern Gong
# Project Title: MSCS532_Assignment1
# Description: This program implements the insertion sort algorithm to sort a list of integers in monotonically decreasing order. 
# If the current value, the key, is equal to a value already in the sorted portion, the equal value is not moved because the 
# program only moves values that are smaller than the key. The key is placed after the equal values already there.

# Insertion sort explanation: The insertion sort algorithm works by dividing the list into a sorted portion and an unsorted portion.
# The first element forms the initial sorted portion, so the algorithm starts processing the second element. The algorithm then 
# goes through the remaining elements one at a time. Each current element called the key, is compared with the elements before it 
# and inserted into its correct position in the sorted portion of the list.
# To sort the list in decreasing order, elements that are smaller than the key are shifted one position to the right. This makes 
# room for the key to be inserted into the correct position. After each pass, the sorted portion grows by one element until the 
# entire list is arranged from largest to smallest.
# The input is a list of integers, and the output is the same list sorted in decreasing order.
# The algorithm sorts the list in place, so another list does not need to be created.
# Its best-case time complexity is Θ(n) when the list is already in decreasing order. Its average-case and worst-case time 
# complexities are Θ(n^2), where n is the number of elements in the input list.
# This explanation of insertion sort and its running time is based on Cormen et al. (2022, Chapter 2).

def insertion_sort_decreasing_order(arr):

    # The first element is considered sorted with length 1, so start with the second element
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1

        # Move smaller elements one position to the right until the key's correct position is found
        while j >= 0 and arr[j] < key:
            arr[j + 1] = arr[j]
            j -= 1

        # Insert key after the last value greater than or equal to it, or at the beginning if no such value exists
        arr[j + 1] = key

    return arr


def main():

    numbers_arr = [5, 2, 20, 9, 1, 5, 6, 3, 71, 8, 4, 56, 12]

    print("Input array:", numbers_arr)

    sorted_arr = insertion_sort_decreasing_order(numbers_arr)

    print("Array sorted in monotonically decreasing order:", sorted_arr)

if __name__ == "__main__":
    main()