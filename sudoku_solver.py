#SUDOKU SOLVER USING BACKTRACK ALGORITHM
def check_number(num, i, j, board):
    row = board[i]
    col = [temp_row[j] for temp_row in board]
    #box selection
    if i in range(3):
        box_rows = [board[t] for t in range (3)]
    elif i in range(3,6):
        box_rows = [board[t] for t in range (3, 6)]
    elif i in range(6,9):
        box_rows= [board[t] for t in range (6,9)]

    if j in range(3):
        box = [t[:3] for t in box_rows]
    elif j in range(3,6):
        box = [t[3:6] for t in box_rows]
    elif j in range(6,9):
        box = [t[6:9] for t in box_rows]
    #flattening box
    box = [y for x in box for y in x]
    # Check num
    if num in row or num in col or num in box:
        return False
    return True

def find_zero(board, N):
    for i in range(N):
        for j in range(N):
            if board[i][j] == 0:
                return i, j #position of the next zero
    return None
    
def solve(board, N):
    #N = dimension
    #exit condition
    pos = find_zero(board, N)
    if pos is None: 
        return True
    else:
        i, j = pos
    for num in range(1, 10):
        if check_number(num, i, j, board):
            board[i][j] = num
            if solve(board, N):
                return True
            board[i][j] = 0
    return False

board = [
    [8, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 3, 6, 0, 0, 0, 0, 0],
    [0, 7, 0, 0, 9, 0, 2, 0, 0],
    [0, 5, 0, 0, 0, 7, 0, 0, 0],
    [0, 0, 0, 0, 4, 5, 7, 0, 0],
    [0, 0, 0, 1, 0, 0, 0, 3, 0],
    [0, 0, 1, 0, 0, 0, 0, 6, 8],
    [0, 0, 8, 5, 0, 0, 0, 1, 0],
    [0, 9, 0, 0, 0, 0, 4, 0, 0]
]

s = solve(board, 9)
print(s)
print(board)