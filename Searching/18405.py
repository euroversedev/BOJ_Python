import sys
from collections import deque

N, K = map(int, sys.stdin.readline().strip().split())
board = [list(map(int, sys.stdin.readline().strip().split()))
        for _ in range(N)]

S, answer_y, answer_x = map(int, sys.stdin.readline().strip().split())

# bfs
q = []
for i in range(N):
    for j in range(N):
        if board[i][j] != 0:
            q.append((board[i][j], i, j, 0))

q = deque(sorted(q))

while q:
    num, y, x, time = q.popleft()
    
    if time == S:
        print(board[answer_y-1][answer_x-1])
        break
    
    for dy, dx in [(0,1),(1,0),(-1,0),(0,-1)]:
        if 0<=y+dy<N and 0<=x+dx<N:
            if board[y+dy][x+dx] == 0:
                board[y+dy][x+dx] = num
                q.append((num, y+dy, x+dx, time+1))
print(board[answer_y-1][answer_x-1])