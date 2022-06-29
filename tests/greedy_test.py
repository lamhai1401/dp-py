from typing import List
import unittest

# from greedy import Graph
from greedy import sequencing_problem, sequencing_problem_with_heap, disjoin_set, loss_inimization, loss_inimization_strategy, build_huffman_tree


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

        self.assertTrue(["a", "c", "e"] != sequencing_problem(arr, 3))

    def test_job_sequen_number_with_heap(self):
        # Driver COde
        arr = [
            ["a", 2, 100],  # Job Array
            ["b", 1, 19],
            ["c", 2, 27],
            ["d", 1, 25],
            ["e", 3, 15],
        ]

        sequencing_problem_with_heap(arr)

    def test_disjoin_set(self):
        arr = [{'id': 'a', 'deadline': 2, 'profit': 100},
        {'id': 'b', 'deadline': 1, 'profit': 19},
        {'id': 'c', 'deadline': 2, 'profit': 27},
        {'id': 'd', 'deadline': 1, 'profit': 25},
        {'id': 'e', 'deadline': 3, 'profit': 15}]

        self.assertTrue(["a", "c", "e"] == disjoin_set(arr))

    def test_loss_minimization(self):
        l: List = [1, 2, 3, 5, 6]
        t: List = [2, 4, 1, 3, 2]

        # self.assertTrue([3, 5, 4, 1, 2] == loss_inimization(l, t))

    def test_loss_inimization_strategy(self):
        arr = [3, 5, 4, 1, 2, 7, 6, 8, 9, 10]
        p = 0.1

        self.assertTrue(41.3811 == loss_inimization_strategy(arr, p))

    def test_huffman_tree_coding(self):
        # characters for huffman tree
        chars = ['a', 'b', 'c', 'd', 'e', 'f']

        # frequency of characters
        freq = [ 5, 9, 12, 13, 16, 45]


        self.assertTrue(['0', '100', '101', '1100', '1101', '111'] == build_huffman_tree(frecs=freq, symbol=chars))

