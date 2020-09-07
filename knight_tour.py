def is_safe(i, j, N, board):
    if i >= 0 and j >= 0 and i < N and j < N and board[i][j] == -1:
        return True
    return False


def solve(board, k_i, k_j, val, move_x, move_y, N):
    #k_i and k_j is the position of the knight
    if val == N*N:
        return True
    for i in range(8): 
        m_i = k_i + move_x[i]
        m_j = k_j + move_y[i]
        if is_safe(m_i, m_j, N, board):
            board[m_i][m_j] = val
            if solve(board, m_i, m_j, val+1, move_x, move_y, N):
                return True
            #Going back
            board[m_i][m_j] = -1
    return False
    
N = 8    
board = [[-1 for i in range(N)]for i in range(N)]
board[0][0] = 0
move_x = [2, 1, -1, -2, -2, -1, 1, 2] 
move_y = [1, 2, 2, 1, -1, -2, -2, -1] 
val = 1
solve(board, 0, 0, val, move_x, move_y, N)
print(board)