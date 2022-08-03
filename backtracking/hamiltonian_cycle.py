# Create an empty matrix with [0][0]
# add first vertex is [0][0] = 1
# loop when 1 -> V and check
# Python program for solution of
# hamiltonian cycle problem

class Graph():
    def __init__(self, vertices):
        self.graph = [[0 for column in range(vertices)]
                            for row in range(vertices)]
        self.v = vertices

    ''' Check if this vertex is an adjacent vertex
    of the previously added vertex and is not
    included in the path earlier '''
    def is_safe(self, v, pos, path):
        # Check if current vertex and last vertex
        # in path are adjacent
        if self.graph[ path[pos-1] ][v] == 0:
            return False

        # Check if current vertex is already in path
        for vertex in path:
            if vertex == v:
                return False

        return True

    def print_solution(self, path):
        print ("Solution Exists: Following",
                "is one Hamiltonian Cycle")
        for vertex in path:
            print (vertex, end = " ")
        print (path[0], "\n")

    # A recursive utility function to solve
    # hamiltonian cycle problem
    def hamcycle_util(self, path, pos):
        # base case: if all vertices are
        # included in the path
        if pos == self.v:
            # Last vertex must be adjacent to the
            # first vertex in path to make a cycle
            if self.graph[ path[pos-1] ][ path[0] ] == 1:
                return True
            else:
                return False

        # Try different vertices as a next candidate
        # in Hamiltonian Cycle. We don't try for 0 as
        # we included 0 as starting point in hamCycle()
        for v in range(1,self.v):
            if self.is_safe(v, pos, path) is True:
                path[pos] = v

                if self.hamcycle_util(path, pos+1) is True:
                    return True

                # Remove current vertex if it doesn't
                # lead to a solution
                path[pos] = -1

        return False

    def ham_cycle(self):
        path = [-1] * self.v
        ''' Let us put vertex 0 as the first vertex
            in the path. If there is a Hamiltonian Cycle,
            then the path can be started from any point
            of the cycle as the graph is undirected '''
        path[0] = 0

        if self.hamcycle_util(path,1) is False:
            print ("Solution does not exist\n")
            return False

        self.print_solution(path)
        return True

''' Let us create the following graph
    (0)--(1)--(2)
    | / \ |
    | / \ |
    | /     \ |
    (3)-------(4) '''
g1 = Graph(5)
g1.graph = [ [0, 1, 0, 1, 0], [1, 0, 1, 1, 1],
            [0, 1, 0, 0, 1,],[1, 1, 0, 0, 1],
            [0, 1, 1, 1, 0], ]

# Print the solution
g1.ham_cycle()

''' Let us create the following graph
    (0)--(1)--(2)
    | / \ |
    | / \ |
    | /     \ |
    (3)     (4) '''
g2 = Graph(5)
g2.graph = [ [0, 1, 0, 1, 0], [1, 0, 1, 1, 1],
        [0, 1, 0, 0, 1,], [1, 1, 0, 0, 0],
        [0, 1, 1, 0, 0], ]

# Print the solution
g2.ham_cycle()