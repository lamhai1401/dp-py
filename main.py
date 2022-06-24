"""
high level support for doing this and that.
"""

from greedy import Graph, sequencing_problem

if __name__ == "__main__":
    # Driver COde
    arr = [
        ["a", 2, 100],  # Job Array
        ["b", 1, 19],
        ["c", 2, 27],
        ["d", 1, 25],
        ["e", 3, 15],
    ]

    # Function Call
    print("Following is maximum profit sequence of jobs")

    sequencing_problem(arr, 3)
