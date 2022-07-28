from typing import List

n = 8


def the_knight_tour_1(matrix: List, row, col, length, result: List):

    if row < 0 or col < 0 or row > length or col > length:
        return result

    if matrix[row][col]:
        result.append((row, col))

    result1 = the_knight_tour_1(matrix, row-2, col+1, length, result.copy())
    result2 = the_knight_tour_1(matrix, row-2, col-1, length, result.copy())

    result3 = the_knight_tour_1(matrix, row+2, col+1, length, result.copy())
    result4 = the_knight_tour_1(matrix, row+2, col-1, length, result.copy())

    result5= the_knight_tour_1(matrix, row+1, col-2, length, result.copy())
    result6= the_knight_tour_1(matrix, row+1, col+2, length, result.copy())

    result7= the_knight_tour_1(matrix, row-1, col+2, length, result.copy())
    result8= the_knight_tour_1(matrix, row-1, col-2, length, result.copy())


    total = [result1, result2, result3, result4, result5, result6, result7, result8]


    max_length = 0
    index = 0
    for i in range(total):
        if len(total[i]) > max_length:
            max_length = len(total[i])
            index = i

    print(total[index])

def is_safe(x, y, board):
    '''
        A utility function to check if i,j are valid indexes
        for N*N chessboard
    '''
    if(x >= 0 and y >= 0 and x < n and y < n and board[x][y] == -1):
        return True
    return False

def print_solution(n, board):
    '''
        A utility function to print Chessboard matrix
    '''
    for i in range(n):
        for j in range(n):
            print(board[i][j], end=' ')
        print()

def solve_kt_util(n, board, curr_x, curr_y, move_x, move_y, pos):
    '''
        A recursive utility function to solve Knight Tour
        problem
    '''

    if pos == n**2:
        return True

    # Try all next moves from the current coordinate x, y
    for i in range(8):
        new_x = curr_x + move_x[i]
        new_y = curr_y + move_y[i]

        if is_safe(new_x, new_y, board):
            board[new_x][new_y] = pos

            if solve_kt_util(n, board, new_x, new_y, move_x, move_y, pos+1):
                return True

            # Backtracking
            board[new_x][new_y] = -1

    return False


def solve_kt(n):
    # Initialization of Board matrix
    board = [[-1 for i in range(n)]for i in range(n)]

    # move_x and move_y define next move of Knight.
    # move_x is for next value of x coordinate
    # move_y is for next value of y coordinate
    move_x = [2, 1, -1, -2, -2, -1, 1, 2]
    move_y = [1, 2, 2, 1, -1, -2, -2, -1]

    # Since the Knight is initially at the first block
    board[0][0] = 0

    # Step counter for knight's position
    pos = 1

    # Checking if solution exists or not
    if not solve_kt_util(n, board, 0, 0, move_x, move_y, pos):
        print("Solution does not exist")
    else:
        print_solution(n, board)


# Function Call
solve_kt(n)
