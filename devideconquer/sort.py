import re
from typing import Dict, List

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

def quick_sort_3partition(sorting: list, left: int, right: int):
    if right <= left:
        return
    a = i = left
    b = right
    pivot = sorting[left]
    while i <= b:
        if sorting[i] < pivot:
            sorting[a], sorting[i] = sorting[i], sorting[a]
            a += 1
            i += 1
        elif sorting[i] > pivot:
            sorting[b], sorting[i] = sorting[i], sorting[b]
            b -= 1
        else:
            i += 1
    quick_sort_3partition(sorting, left, a - 1)
    quick_sort_3partition(sorting, b + 1, right)

array = [0, 5, 3, 2, 2]
quick_sort_3partition(array, 0, len(array)-1)
print(f'Sorted array: {array}')

# to find a root
def find(parent, num):
    if parent[num] == num:
        return num
    else:
        parent[num] = find(parent, parent[num])
        return parent[num]

def minimum_number_of_platforms(arrival: List, deps: List, n):
    arrival = sorted(arrival)
    deps = sorted(deps)

    arr: List = [()] * n

    # save each pair start/stop
    for i in range(0, n,1):
        arr[i] = (arrival[i], deps[i])


    result: List = []
    check: Dict = {}

    for i in range(0, n, 1):
        # checked duplicated
        if check.get(i, False):
            continue
        check[i] = True
        data: List = [arr[i]]
        last = arr[i] # save last data
        for j in range(i+1, n, 1):
            if check.get(j, False):
                continue
            if last[1] < arr[j][0]:
                data.append(arr[j])
                check[j] = True
                last = arr[j]
        result.append(data)
    return len(result)

def minimum_number_of_coins(coins: List, total):
    # sorted coind
    temp = total
    coins = sorted(coins, reverse=True)
    result: Dict = {}

    i = 0

    while i < len(coins):
        if coins[i] > total:
            i+=1
            continue
        if (total - coins[i]) >= 0:
            total = total - coins[i]
            saved = result.get(coins[i], 0)
            if saved == 0:
                result[coins[i]] = 1
            else:
                result[coins[i]] = result[coins[i]]+1
            if total == 0:
                break


    data = 0
    for _,key in enumerate(result.keys()):
        data = data + (key * result.get(key))

    print("Total after: ", data)
    print("Rem after: ", data - temp)
    return result

    # lst: List = [1, 2, 5, 10, 20, 50, 100, 500, 1000]
    # print(minimum_number_of_coins(lst, 9435347))
