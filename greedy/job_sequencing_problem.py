from typing import List
import heapq


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

def sequencing_problem_with_heap(arr):
    length_arr = len(arr) # find arr len

    result: List = []
    max_heap: List = []


    # sorted current arr with increasing deadline
    arr = sorted(arr, key=lambda item: item[1])

    for i in range(length_arr-1,-1,-1):

        if i == 0:
            slot_avail = arr[i][1]
        else:
            slot_avail = arr[i][1] - arr[i-1][1]

        heapq.heappush(max_heap, (-arr[i][2], arr[i][1], arr[i][0]))

        while slot_avail and max_heap:
            _, _, job_id = heapq.heappop(max_heap)
            result.append(job_id)
            slot_avail -=1

    print(result)
