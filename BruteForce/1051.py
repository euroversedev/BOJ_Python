import sys

N, M = map(int, sys.stdin.readline().strip().split())
board = [list(map(int, sys.stdin.readline().strip())) for _ in range(N)]

max_size = 0
for y in range(N):
    for x in range(M):
        
        i = 0
        while y+i<N and x+i<M:
            if board[y][x] == board[y+i][x] \
            and board[y][x] == board[y][x+i] \
            and board[y][x] == board[y+i][x+i]:
                max_size = max(max_size, (i+1)**2)
            
            i += 1
print(max_size)