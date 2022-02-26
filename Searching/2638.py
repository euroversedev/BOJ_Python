import sys
from collections import deque

N, M = map(int, input().split())
board = [list(map(int, sys.stdin.readline().strip().split()))
        for _ in range(N)]


def bfs(i, j):
    board[i][j] = 2
    q = deque([(i, j)])
    
    while q:
        y, x = q.popleft()
        
        for dy, dx in [(1,0),(-1,0),(0,1),(0,-1)]:
            if 0<=y+dy<N and 0<=x+dx<M:
                if board[y+dy][x+dx] == 0:
                    board[y+dy][x+dx] = 2
                    q.append((y+dy, x+dx))
    
# 외부 공기를 2로 표현
bfs(1, 1)

time = 0
while True:
    
    tmp = []
    
    for i in range(1, N-1):
        for j in range(1, M-1):
            if board[i][j] == 1:
                cnt = 0
                for dy, dx in [(1,0),(-1,0),(0,1),(0,-1)]:
                    if board[i+dy][j+dx] == 2: cnt += 1
                if cnt > 1:
                    tmp.append((i, j))
    
    if len(tmp) == 0: break
    
    for i, j in tmp:
        bfs(i, j)
        
    time += 1
    
print(time)