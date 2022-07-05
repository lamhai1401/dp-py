
# Python3 program to find efficient
# solution for the network

# number of houses and number
# of pipes
from typing import List


n_of_houses = 0
p_of_pines = 0

# Array rd stores the
# ending vertex of pipe
rd = [0]*1100

# Array wd stores the value
# of diameters between two pipes
wt = [0]*1100

# Array cd stores the
# starting end of pipe
cd = [0]*1100

# List a, b, c are used
# to store the final output
a = []
b = []
c = []

ans = 0


def dfs(w):
    global ans

    if (cd[w] == 0):
        return w

    if (wt[w] < ans):
        ans = wt[w]

    return dfs(cd[w])

# Function performing calculations.
def solve(arr: List, p_of_pines, n_of_houses):
    global ans
    i = 0

    # init data
    while i < p_of_pines:

        q = arr[i][0]
        h = arr[i][1]
        t = arr[i][2]

        cd[q] = h
        wt[q] = t
        rd[h] = q
        i += 1

    a = []
    b = []
    c = []

    '''If a pipe has no ending vertex
    but has starting vertex i.e is
    an outgoing pipe then we need
    to start DFS with this vertex.'''
    for j in range(1, n_of_houses + 1):
        if (rd[j] == 0 and cd[j]):

            ans = 1000000000
            w = dfs(j)

            # We put the details of component
            # in final output array
            a.append(j)
            b.append(w)
            c.append(ans)

    result: List = []
    for j, value in enumerate(a):
        result.append([value, b[j], c[j]])

    return result