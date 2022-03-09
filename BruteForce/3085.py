import sys

N = int(input())
board = [list(sys.stdin.readline()) for _ in range(N)]

def find_max(board):
    pre = 'X'
    max_ = 0
    
    for y in range(N):
        cnt = 0
        for x in range(N):
            if board[y][x] != pre:
                max_ = max(max_, cnt)
                cnt = 1
                pre = board[y][x]
                continue
            else:
                cnt += 1
        max_ = max(max_, cnt)
    
    for x in range(N):
        cnt = 0
        for y in range(N):
            if board[y][x] != pre:
                max_ = max(max_, cnt)
                cnt = 1
                pre = board[y][x]
                continue
            else:
                cnt += 1
        max_ = max(max_, cnt)
    
    return max_
    
# 세로
max_ = 0
for y in range(N-1):
    for x in range(N):
        if board[y][x] != board[y+1][x]:
            board[y][x], board[y+1][x] = board[y+1][x], board[y][x]
            max_ = max(max_, find_max(board))
            board[y][x], board[y+1][x] = board[y+1][x], board[y][x]
        

# 가로
for y in range(N):
    for x in range(N-1):
        if board[y][x] != board[y][x+1]:
            board[y][x], board[y][x+1] = board[y][x+1], board[y][x]
            max_ = max(max_, find_max(board))
            board[y][x], board[y][x+1] = board[y][x+1], board[y][x]
print(max_)