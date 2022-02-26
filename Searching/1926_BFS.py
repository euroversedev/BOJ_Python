import sys
from collections import deque

N, M = map(int, input().split())
board = [list(map(int, sys.stdin.readline().strip().split()))
        for _ in range(N)]

def bfs(i, j):
    board[i][j] = 0
    q = deque([(i, j)])
    
    result = 1
    while q:
        y, x = q.popleft()
        
        for dy, dx in [(1,0),(-1,0),(0,1),(0,-1)]:
            if 0<=y+dy<N and 0<=x+dx<M:
                if board[y+dy][x+dx] == 1:
                    board[y+dy][x+dx] = 0
                    q.append((y+dy, x+dx))
                    result += 1
                    
    return result 

cnt = 0
max_ = 0
for i in range(N):
    for j in range(M):
        if board[i][j] ==1:
            cnt+=1
            result = bfs(i, j)
            if result > max_: max_ = result
                
print(cnt, max_, sep='\n')