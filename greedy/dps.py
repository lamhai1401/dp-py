
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




# Python3 program to find maximum
# number of thieves caught

# Returns maximum number of thieves
# that can be caught.
def police_thief(arr, n, k):

    thief: List = []
    police: List = []
    l = 0
    r = 0
    # to save result
    result:List = []

    for key, value in enumerate(arr):
        if value == 'T':
            thief.append(key)
        elif value == 'P':
            police.append(key)


    # track lowest current indices of
    # thief: thi[l], police: pol[r]
    while l < len(thief) and r < len(police):
        if abs(thief[l] - police[r]) <= k:
            result.append([thief[l], police[r]])
            l+=1
            r+=1
        elif thief[l] > police[r]:
            r+=1
        else:
            l+=1


    return len(result)


def bracket_balancing(s:List):
    # Swap stores the number of swaps
    # required imbalance maintains the
    # number of imbalance pair
    swap = 0
    imbalance = 0

    for i in s:
        if i == '[':

            # Decrement the imbalance
            imbalance -= 1
        else:

            # Increment imbalance
            imbalance += 1

            if imbalance > 0:
                swap += imbalance

    return swap

def fitting_shelves_problem(w, m, n):
    num_m = 0
    num_n = 0

    p = w//m
    q = 0
    rem=w%m
    num_m=p
    num_n=q
    min_empty=rem


    # calculate num m,n
    while w >= n:
        w -= n
        p = w // m
        q += 1
        r = w % m # calculate rem of current w
        if r <= rem:
            num_m = p
            num_n = q
            rem = r
    return (num_m, num_n, rem)


def mice_to_holes(num_mice: List, num_hole: List):
    # sorting
    num_mice = sorted(num_mice)
    num_hole = sorted(num_hole)

    maxi = 0

    length = len(num_mice)

    for i in range(length):
        rem = num_hole[i] - num_mice[i]
        if rem > maxi:
            maxi = rem

    return maxi

