# A utility function to check if a queen can
# be placed on board[row][col]. Note that this
# function is called when "col" queens are
# already placed in columns from 0 to col -1.
# So we need to check only left side for
# attacking queens

def is_valid(board, queen, row, col):
    # Check this row on left side
    for i in range(col):
        if board[row][i] == 1:
            return False

    # Check upper diagonal on left side
    for i, j in zip(range(row, -1, -1),
                    range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    # Check lower diagonal on left side
    for i, j in zip(range(row, queen, 1),
                    range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    return True

def n_queen_utils(board, queen: int, col: int):
    # base case: If all queens are placed
    # then return true
    if col >= queen:
        return True

    # Consider this column and try placing
    # this queen in all rows one by one
    for i in range(queen):
        if is_valid(board, queen, i, col):
            # Place this queen in board[i][col]
            board[i][col] = 1

            # recur to place rest of the queens
            if n_queen_utils(board, queen, col + 1):
                return True

            # If placing queen in board[i][col
                        # doesn't lead to a solution, then
                        # queen from board[i][col]
            board[i][col] = 0

def print_solution(board, queen):
    for i in range(queen):
        for j in range(queen):
            print(board[i][j], end = " ")
        print()

def solve_n_q():
    board = [
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0],
        ]

    if n_queen_utils(board, 4, 0) is False:
        print ("Solution does not exist")
        return False

    print_solution(board, 4)
    return True


solve_n_q()

# TODO re write because queen cannot place at the same row
