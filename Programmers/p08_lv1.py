def solution(board, h, w):
    
    answer = 0
    
    # 상하좌우에 칸이 있는지 확인하고, 있다면 색깔 검사
    if (h - 1) >= 0:
        if board[h - 1][w] == board[h][w]: answer = answer + 1
    if (h + 1) < len(board):
        if board[h + 1][w] == board[h][w]: answer = answer + 1
    if (w - 1) >= 0:
        if board[h][w - 1] == board[h][w]: answer = answer + 1
    if (w + 1) < len(board):
        if board[h][w + 1] == board[h][w]: answer = answer + 1
    
    return answer