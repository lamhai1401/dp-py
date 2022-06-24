from typing import List


def sequencing_problem(arr, t_jobs):
    length_arr = len(arr)

    # sorting
    arr = sorted(arr, reverse=True, key=lambda item: item[2])

    print(arr)

    result: List = ["-1"] * t_jobs

    rank = [False] * t_jobs

    for index_job in range(0, length_arr):
        for j in range(min(arr[index_job][1] - 1, t_jobs - 1), -1, -1):
            print("j", j, "\n")
            if rank[j] is False:
                rank[j] = True
                result[j] = arr[index_job][0]

    print(result)
    return result
