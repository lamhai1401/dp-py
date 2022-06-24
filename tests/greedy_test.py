import unittest

# from greedy import Graph
from greedy import sequencing_problem


class GreedyTest(unittest.TestCase):
    # def test_mst(self):
    #     # Driver code
    #     g = Graph(4)
    #     g.add_edge(0, 1, 10)
    #     g.add_edge(0, 2, 6)
    #     g.add_edge(0, 3, 5)
    #     g.add_edge(1, 3, 15)
    #     g.add_edge(2, 3, 4)

    #     # Function call
    #     g.KruskalMST()

    def test_job_sequen_number(self):
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

        self.assertTrue(["a", "c", "e"] == sequencing_problem(arr, 3))
