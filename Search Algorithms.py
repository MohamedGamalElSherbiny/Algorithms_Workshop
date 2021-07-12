# Binary Search Algorithm:
def binary_search(array, target_value):
    """
    Finds the index of an item in an array using binary search algorithm

    Parameters:
    ----------
    array :          list
                     List of elements
    target_value:    object
                     The item to search for in the array

    Returns:
    --------
    If found: String containing the number of iterations.
              String containing the  index of the element.

    Else:     String
    """
    minimum = 0
    maximum = len(array) - 1
    guess_total = 0
    while maximum >= minimum:
        guess = (maximum + minimum) // 2
        guess_total += 1
        if array[guess] == target_value:
            print("Number of guesses is {}".format(guess_total))
            return "Item {} is in the list, at index: {}.".format(target_value, guess)
        elif array[guess] < target_value:
            minimum = guess + 1
        else:
            maximum = guess - 1
    return "Item {} is not in the list.".format(target_value)

# Linear Search Algorithm:
def linear_search(array, target_value):
    """
    Finds the index of an item in an array using linear search algorithm

    Parameters:
    ----------
    array :          list
                     List of elements
    target_value:    object
                     The item to search for in the array

    Returns:
    --------
    If found: String containing the number of iterations.
              String containing the  index of the element.

    Else:     String
    """
    guess_total = 0
    for i in range(len(array)):
        guess_total += 1
        if array[i] == target_value:
            print("Number of guesses is {}".format(guess_total))
            return "Item {} is in the list, at index: {}.".format(target_value, i)
    return "Item {} is not in the list.".format(target_value)

lst = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
print(binary_search(lst, 73))
print(linear_search(lst, 73))