import sys
from collections import deque

M, N = map(int, sys.stdin.readline().strip().split())
board = [list(sys.stdin.readline().strip()) for _ in range(N)]

power = {'W':0, 'B':0}

for i in range(N):
    for j in range(M):

        if board[i][j] in ['W', 'B']:
            
            color = board[i][j]
            board[i][j] = 'X'
            cnt = 1
            q = deque([(i, j)])
            while q:
                y, x = q.popleft()
                
                for dy, dx in [(1,0),(0,1),(-1,0),(0,-1)]:
                    if 0<=y+dy<N and 0<=x+dx<M and board[y+dy][x+dx] == color:
                        board[y+dy][x+dx] = 'X'
                        q.append((y+dy, x+dx))
                        cnt += 1
            
            power[color] += cnt*cnt
            
print(power['W'], power['B'])