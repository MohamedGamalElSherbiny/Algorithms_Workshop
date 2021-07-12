# Selection Sort Algorithm
def swap(array, first_index, second_index):
    """
    Swaps two elements in a list

    Parameters:
    ----------
    lst :          list
                   List of numbers
    first_index:   integer
                   The first number index
    second_index:  integer
                   The first number index
    """
    temp = array[first_index]
    array[first_index] = array[second_index]
    array[second_index] = temp

def find_minimum(array, index):
    """
    Find the minimum number in a list

    Parameters:
    ----------
    lst :          list
                   List of numbers
    index :        integer
                   The index of the number

    Returns:
    --------
    min_index :    integer
                   The index of the minimum number
    """
    min_value = array[index]
    min_index = index
    for i in range(index + 1, len(array)):
        if array[i] < min_value:
            min_index = i
            min_value = array[i]
    return min_index

def selection_sort(array):
    """
    Sort an array of numbers using Selection Sort Algorithm

    Parameters:
    ----------
    array :        list
                   List of numbers

    Returns:
    --------
    array :        list
                   Sorted list
    """
    for i in range(len(array)):
        element = find_minimum(array, i)
        swap(array, element, i)
    return array

# Insertion Sort
def insertion_sort(array):
    """
    Sort an array of numbers using Insertion Sort Algorithm

    Parameters:
    ----------
    array :        list
                   List of numbers

    Returns:
    --------
    array :        list
                   Sorted list
    """
    for i in range(1, len(array)):
        key = array[i]
        j = i - 1
        while j >= 0 and key < array[j]:
            array[j + 1] = array[j]
            j -= 1
        array[j + 1] = key
    return array

#  Merge Sort Algorithm
def merge_sort(array):
    """
    An Algorithmic function that returns the sorted array

    Parameters:
    ----------

    array : list
            A list of unsorted integers

    Returns:
    -------

    array : list
            A list of sorted integers

    See Also:
    --------

    https://en.wikipedia.org/wiki/Merge_sort

    This algorithm was developed to return a sorted list of integers in ascending order.

    It uses Divide and Conquer Algorithm with complexity = O(n log n)

    In this function the while loop is used.
    """
    if len(array) > 1:
        mid = len(array) // 2
        left_array = array[:mid]
        right_array = array[mid:]
        merge_sort_while(left_array)
        merge_sort_while(right_array)
        i = j = k = 0
        for _ in range(len(left_array) + len(right_array)):
            if i == len(left_array):
                array[k] = right_array[j]
                j += 1
                k += 1
            elif j == len(right_array):
                array[k] = left_array[i]
                i += 1
                k += 1
            else:
                if left_array[i] < right_array[j]:
                    array[k] = left_array[i]
                    i += 1
                    k += 1
                elif left_array[i] > right_array[j]:
                    array[k] = right_array[j]
                    j += 1
                    k += 1
    return array

def merge_sort_while(array):
    """
    An Algorithmic function that returns the sorted array

    Parameters:
    ----------

    array : list
            A list of unsorted integers

    Returns:
    -------

    array : list
            A list of sorted integers

    See Also:
    --------

    https://en.wikipedia.org/wiki/Merge_sort

    This algorithm was developed to return a sorted list of integers in ascending order.

    It uses Divide and Conquer Algorithm with complexity = O(n log n)

    In this function the while loop is used.
    """
    if len(array) > 1:
        mid = len(array) // 2
        left_array = array[:mid]
        right_array = array[mid:]
        merge_sort_while(left_array)
        merge_sort_while(right_array)
        i = j = k = 0
        while len(left_array) > i and len(right_array) > j:
            if left_array[i] < right_array[j]:
                array[k] = left_array[i]
                i += 1
            else:
                array[k] = right_array[j]
                j += 1
            k += 1
        while len(left_array) > i:
            array[k] = left_array[i]
            i += 1
            k += 1
        while len(right_array) > j:
            array[k] = right_array[j]
            j += 1
            k += 1
    return array

lst = [3, 8, 1, 0, 4, 9, 7]
lst_copy = lst.copy()
print("My original array was:\n{}\n\nAnd after Selection sort is:\n{}\n".format(lst, selection_sort(lst_copy)))
lst_copy = lst.copy()
print("My original array was:\n{}\n\nAnd after Insertion sort is:\n{}\n".format(lst, insertion_sort(lst_copy)))
lst_copy = lst.copy()
print("My original array was:\n{}\n\nAnd after Merge sort is:\n{}\n".format(lst, merge_sort(lst_copy)))
lst_copy = lst.copy()
print("My original array was:\n{}\n\nAnd after Merge sort using While is:\n{}\n".format(lst, merge_sort_while(lst_copy)))