"""Implement quick sort in Python.
Input a list.
Output a sorted list."""
def quicksort(array, start = 0, end=None):
    if end == None:
        end = len(array) - 1
    if end - start < 1:
        return array
    else:
        length = len(array)
        pivot_index = end
        store_index = end - 1
        pivot = array[pivot_index]
        for i in range(0, end+1):
            if i<pivot_index:
                while array[i] > array[pivot_index]:
                    array[pivot_index] = array[i]
                    array[i] = array[store_index]
                    array[store_index] = pivot
                    pivot_index = store_index
                    store_index -= 1
        a = quicksort(array, start, pivot_index - 1)
        b = quicksort(array, pivot_index + 1, end)
        return array

test = [21, 4, 1, 3, 9, 20, 25, 6, 21, 14]
print quicksort(test)
