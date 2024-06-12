def is_safe(board, row, col):
    # Check this row on the left side
    for i in range(col):
        if board[row][i]:
            return False

    # Check upper diagonal on the left side
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j]:
            return False

    # Check lower diagonal on the left side
    for i, j in zip(range(row, len(board), 1), range(col, -1, -1)):
        if board[i][j]:
            return False

    return True

def solve_queens(board, col):
    if col >= len(board):
        return True
    
    for i in range(len(board)):
        if is_safe(board, i, col):
            board[i][col] = 1
            if solve_queens(board, col + 1):
                return True
            board[i][col] = 0
    
    return False

def place_queens():
    board = [[0] * 8 for _ in range(8)]
    if solve_queens(board, 0):
        print("Solution:")
        for row in board:
            print(" ".join(str(x) for x in row))
    else:
        print("No solution exists")

if _name_ == "_main_":
    place_queens()
    
    OUTPUT
    >>> %Run lol.py
Solution:
1 0 0 0 0 0 0 0
0 0 0 0 0 0 1 0
0 0 0 0 1 0 0 0
0 0 0 0 0 0 0 1
0 1 0 0 0 0 0 0
0 0 0 1 0 0 0 0
0 0 0 0 0 1 0 0
0 0 1 0 0 0 0 0
>>>
