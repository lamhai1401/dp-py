from hashlib import new
from shutil import move
from typing import List

def is_valid(n, maze, x, y, res):
    if x >= 0 and y >= 0 and x < n and y < n and maze[x][y] == 1 and res[x][y] == 0:
        return True
    return False

def rat_maze(n, maze, move_x, move_y, x, y, res):
    # if (x, y is goal) return True
    if x == n-1 and y == n-1:
        return True

    for i in range(n):
        new_x = move_x[i] + x
        new_y = move_y[i] + y

        if is_valid(n, maze, new_x, new_y, res):
            res[new_x][new_y] = 1
            if rat_maze(n, maze, move_x, move_y, new_x, new_y, res):
                return True
            res[new_x][new_y] = 0
    return False

def rat_in_a_maze(maze, n):
    # Initialization of Board matrix
    # Creating a 4 * 4 2-D list
    res = [[0 for i in range(n)] for i in range(n)]
    res[0][0] = 1

    # x matrix for each direction
    move_x = [-1, 1, 0, 0]

    # y matrix for each direction
    move_y = [0, 0, -1, 1]

    if rat_maze(n, maze, move_x, move_y, 0, 0, res):
        for i in range(n):
            for j in range(n):
                print(res[i][j], end=' ')
            print()
    else:
        print('Solution does  not exist')


# Initialising the maze
maze = [[1, 0, 0, 0],
            [1, 1, 0, 1],
            [0, 1, 0, 0],
            [1, 1, 1, 1]]

rat_in_a_maze(maze, 4)
