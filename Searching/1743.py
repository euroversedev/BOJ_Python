import sys
from collections import deque

N, M, K = map(int, sys.stdin.readline().strip().split())
board = [[False] * (M+1) for _ in range(N+1)]

for _ in range(K):
    y, x = map(int, sys.stdin.readline().strip().split())
    board[y][x] = True
    
    
# 면적 구하기
max_size = 0
for i in range(1, N+1):
    for j in range(1, M+1):
        if board[i][j] == True:
            
            size = 1
            
            # bfs
            board[i][j] = False
            q = deque([(i, j)])
            
            while q:
                y, x = q.popleft()
                
                for dy, dx in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    if 0<y+dy<=N and 0<x+dx<=M:
                        if board[y+dy][x+dx] == True:
                            board[y+dy][x+dx] = False
                            q.append((y+dy, x+dx))
                            size += 1
            
            if size > max_size: max_size = size
                
print(max_size)