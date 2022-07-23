
from typing import List


def calculate_arr_mid(arr: List, l, m, h):
    # if len(arr) <= 2:
    #     return sum(arr)

    # mid = length // 2

    # left = arr[:mid]
    # right = arr[mid:]

    # max_left = maximum_subarray_sum(left, len(left))
    # max_right = maximum_subarray_sum(right, len(left))

    # total = max_left + max_right

    # Include elements on left of mid.
    sm = 0
    left_sum = -10000

    for i in range(m, l-1, -1):
        sm = sm + arr[i]

        if sm > left_sum:
            left_sum = sm

    # Include elements on right of mid
    sm = 0
    right_sum = -1000
    for i in range(m + 1, h + 1):
        sm = sm + arr[i]

        if sm > right_sum:
            right_sum = sm

    # Return sum of elements on left and right of mid
    # returning only left_sum + right_sum will fail for [-2, 1]
    return max(left_sum + right_sum, left_sum, right_sum)

def maximum_subarray_sum(arr:List, l, h):
    # Base Case: Only one element
    if l == h:
        return arr[l]

    # Find middle point
    m = (l + h) // 2

    # Return maximum of following three possible cases
    # a) Maximum subarray sum in left half
    # b) Maximum subarray sum in right half
    # c) Maximum subarray sum such that the
    #     subarray crosses the midpoint
    return max(
                maximum_subarray_sum(arr, l, m),
                maximum_subarray_sum(arr, m+1, h),
                calculate_arr_mid(arr, l, m, h)
            )


lst: List = [-2, -5, 6, -2, -3, 1, 5, -6]
length = len(lst)
maximum_subarray_sum(lst, 0, length)
