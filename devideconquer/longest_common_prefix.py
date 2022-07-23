from typing import List

def common_prefix_til(str1, str2):
    result = ""
    n1, n2 = len(str1), len(str2)
    i, j = 0, 0

    while i <= n1 - 1 and j <= n2 - 1:
        if str1[i] != str2[j]:
            break
        else:
            result += str1[i]
            i+=1
            j+=1

    return result

def longest_common_prefix(arr: List, left: int, right: int):
    if left == right:
        return arr[left]

    if left < right:

        # mid = (left + right) // 2 same as below
        mid = left + (right - left) // 2

        pre_left = longest_common_prefix(arr, left, mid)
        pre_right = longest_common_prefix(arr, mid+1, right)

        return common_prefix_til(pre_left, pre_right)

temp = ["geeksforgeeks", "geeks", "geek", "geezer"]
n = len(temp)
ans = longest_common_prefix(temp, 0, n - 1)

if len(ans):
    print("The longest common prefix is", ans)
else:
    print("There is no common prefix")
