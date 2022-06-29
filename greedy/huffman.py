from typing import List


class Node:


    def __init__(self, frec, symbol, left=None, right=None):
        self.frec = frec
        self.symbol = symbol
        self.left = left
        self.right = right
        self.trace = ""


def trace_nodes(node: Node, trace, result: List):


    new_trace = trace + node.trace

    if node.left:
        trace_nodes(node.left, new_trace, result)

    if node.right:
        trace_nodes(node.right, new_trace, result)

    if not node.left and not node.right:
        print(f"{node.symbol} -> {new_trace}")
        result.append(new_trace)


def init_nodes(frecs: List, symbol: List):
    nodes: List = []

    for key, value in enumerate(symbol):
        nodes.append(Node(frec=frecs[key], symbol=value, left=None, right=None))


    return nodes

def build_huffman_tree(frecs: List, symbol: List):

    nodes = init_nodes(frecs, symbol)

    left = "0"
    right = "1"

    while len(nodes) > 1:

        # sorted node
        nodes = sorted(nodes, key=lambda item: item.frec)

        node0: Node = nodes[0]
        node0.trace = left
        node1: Node = nodes[1]
        node1.trace = right

        new_node = Node(frec=node0.frec + node1.frec, symbol = node0.symbol + node1.symbol, left=node0, right=node1)

        nodes.remove(node0)
        nodes.remove(node1)
        nodes.append(new_node)

    result: List = []
    trace_nodes(nodes[0], "", result)
    return result
