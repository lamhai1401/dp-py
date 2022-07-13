

from operator import le
from typing import List

def bin_ser(arr, x):
    # sorted arr
    arr = sorted(arr)

    left = 0
    right = len(arr)

    while left <= right:
        rem = (left + right) // 2
        if arr[rem] == x:
            return rem

        elif arr[rem] > x:
            right = rem
        else:
            left = rem

    return -1

def merge_sort(arr: List):
    if len(arr) > 1 :
        # Finding the mid of the array
        mid = len(arr)//2

        left = arr[:mid]
        right = arr[mid:]

        merge_sort(left)
        merge_sort(right)

        i = j = k = 0 # index of list

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                arr[k] = left[i]
                i+=1
            else:
                arr[k] = right[j]
                j+=1
            k+=1

        # Checking if any element was left
        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1
        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1

