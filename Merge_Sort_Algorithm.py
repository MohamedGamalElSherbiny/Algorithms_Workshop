#!/usr/bin/env python
# coding: utf-8

# # Merge Sort:

# ## Using For loop:

# In[1]:


def merge_sort(arr):
    """
    An Algorithmic function that returns the sorted array
    
    Parameters:
        arr : list
              A list of unsorted integers
    Returns:
        arr : list
              A list of sorted integers
    See Also:
    
        https://en.wikipedia.org/wiki/Merge_sort
        
        This algorithm was developed to return a sorted list of integers in ascending order.
        
        It uses Divide and Conquer Algorithm with complexity = O(n logn)
        
        In this function the for loop is used.
    """
    if len(arr) > 1:
        mid = len(arr) // 2
        left_array = arr[:mid]
        right_array = arr[mid:]
        merge_sort_while(left_array)
        merge_sort_while(right_array)
        i = j = k = 0
        i = j = k = 0
        for _ in range(len(left_array) + len(right_array)):
            if i == len(left_array):
                arr[k] = right_array[j]
                j += 1
                k += 1
            elif j == len(right_array):
                arr[k] = left_array[i]
                i += 1
                k += 1
            else:
                if left_array[i] < right_array[j]:
                    arr[k] = left_array[i]
                    i += 1
                    k += 1
                elif left_array[i] > right_array[j]:
                    arr[k] = right_array[j]
                    j += 1
                    k += 1
    return arr


# ## Using While loop:

# In[2]:


def merge_sort_while(arr):
    """
    An Algorithmic function that returns the sorted array
    
    Parameters:
        arr : list
              A list of unsorted integers
    Returns:
        arr : list
              A list of sorted integers
    See Also:
    
        https://en.wikipedia.org/wiki/Merge_sort
        
        This algorithm was developed to return a sorted list of integers in ascending order.
        
        It uses Divide and Conquer Algorithm with complexity = O(n logn)
        
        In this function the while loop is used.
    """
    if len(arr) > 1:
        mid = len(arr) // 2
        left_array = arr[:mid]
        right_array = arr[mid:]
        merge_sort_while(left_array)
        merge_sort_while(right_array)
        i = j = k = 0
        while len(left_array) > i and len(right_array) > j:
            if left_array[i] < right_array[j]:
                arr[k] = left_array[i]
                i += 1
            else:
                arr[k] = right_array[j]
                j += 1
            k += 1
        while len(left_array) > i:
            arr[k] = left_array[i]
            i += 1
            k += 1
        while len(right_array) > j:
            arr[k] = right_array[j]
            j += 1
            k += 1
    return arr


# In[3]:


merge_sort_while([3,8,1,0,4,9,7])


# In[4]:


merge_sort([3,8,1,0,4,9,7])

