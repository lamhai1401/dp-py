from typing import List
import heapq
import sys
from unittest import result

from tomlkit import item


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


class DisjointSet:


    def __init__(self, length) -> None:
            # init parent each job has parent itself
        self.parent = [i for i in range(length+1)]


    def find(self, num):
        if self.parent[num] == num:
            return num
        else:
            self.parent[num] = self.find(self.parent[num])
            return self.parent[num]

    def merge(self, u, v):
        # Update the greatest available
        # free slot to u
        self.parent[v] = u

    def union(self, u,v):
        # check conditionP


        self.parent[v] = u



def cmp(a):
    return a['profit']

def findmaxdeadline(arr, n):
    """
    :param arr: Job array
    :param n: length of array
    :return: maximum deadline from the set of jobs
    """
    ans = - sys.maxsize - 1
    for i in range(n):
        ans = max(ans, arr[i]['deadline'])
    return ans

def disjoin_set(arr):
    # sort by profit
    length_arr = len(arr)
    arr = sorted(arr, key=cmp, reverse=True)
    max_deadline = findmaxdeadline(arr, length_arr)
    ds = DisjointSet(max_deadline)

    result: List = []

    for i in range(length_arr):
        # find maximum available free slot for
        # this job (corresponding to its deadline)
        available_slot = ds.find(arr[i]['deadline'])

        if available_slot > 0:
            # This slot is taken by this job 'i'
            # so we need to update the greatest free slot.
            # Note: In merge, we make first parameter
            # as parent of second parameter.
            # So future queries for available_slot will
            # return maximum available slot in set of
            # "available_slot - 1"
            ds.merge(ds.find(available_slot - 1),
                            available_slot)
            result.append(arr[i]['id'])

    return result
