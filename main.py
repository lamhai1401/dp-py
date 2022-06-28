"""
high level support for doing this and that.
"""

from greedy import Graph, sequencing_problem, sequencing_problem_with_heap, disjoin_set, loss_inimization_strategy

# Driver Code
if __name__ == "__main__":
    # arr = [4, 2, 151, 15, 1, 52, 12]
    arr = [3, 5, 4, 1, 2, 7, 6, 8, 9, 10]
    p = 0.1

    print(loss_inimization_strategy(arr, p))
