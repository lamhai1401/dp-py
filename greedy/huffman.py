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

class Queue:

    def __init__(self):
        self.queue: List = []

    def is_empty(self):
        return len(self.queue) == 0

    def is_size_one(self):
        return len(self.queue) == 1

    # Function to add item to the queue
    def enqueue(self, value):
        self.queue.append(value)

    # Function to remove item from the queue
    def dequeue(self):
        return self.queue.pop(0)


class QueueNode:

    def __init__(self, frec, symbol, left=None, right=None) -> None:
        self.frec = frec
        self.symbol = symbol
        self.left = left
        self.right = right
        self.trace = ""


    # Function to check if the following
    # node is a leaf node
    def is_leaf(self):
        return (self.left is None and self.right is None)


def find_min_node(queue1: Queue, queue2: Queue):

    if queue1.is_empty():
        return queue2.dequeue()

    if queue2.is_empty():
        return queue1.dequeue()

    if queue1.queue[0].frec > queue2.queue[0].frec:
        return queue2.dequeue()

    return  queue1.dequeue()

def huffman_coding_for_sorted_input(frecs: List, symbol: List):
    # create list node first
    queue1: Queue = Queue()
    queue2: Queue = Queue()

    for key, value in enumerate(frecs):
        queue1.enqueue(QueueNode(frec=value, symbol=symbol[key]))

    # queue1 = sorted(queue1, key=lambda item: item.frec)

    left = "0"
    right = "1"

    while not (queue1.is_empty() and queue2.is_size_one()):
        node0 = find_min_node(queue1, queue2)
        node0.trace = left
        node1 = find_min_node(queue1, queue2)
        node1.trace=right

        new_node = QueueNode(frec=(node0.frec + node1.frec), symbol="$", left=node0, right=node1)

        queue2.enqueue(new_node)

    result = []
    trace_nodes(queue2.dequeue(), "", result)
    
    return result
