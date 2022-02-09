import sys
from collections import deque
import copy

N = int(input())
board = [list(sys.stdin.readline().strip()) for _ in range(N)]

def bfs(board, i, j):
    color = board[i][j]
    board[i][j] = 'X'    # 방문처리
    
    q = deque([(i, j, color)])
    while q:
        i, j, color = q.popleft()
        
        for dy, dx in [(1,0),(-1,0),(0,1),(0,-1)]:
            if 0<=i+dy<N and 0<=j+dx<N:
                if board[i+dy][j+dx] == color:
                    board[i+dy][j+dx] = 'X'
                    q.append((i+dy, j+dx, color))
    
copied_board1 = copy.deepcopy(board)
copied_board2 = copy.deepcopy(board)
cnt1 = 0
cnt2 = 0
for i in range(N):
    for j in range(N):
        if copied_board1[i][j] !='X':
            bfs(copied_board1, i, j)
            cnt1 += 1

        
        if copied_board2[i][j] == 'G':
            copied_board2[i][j] = 'R'
            
for i in range(N):
    for j in range(N):
        if copied_board2[i][j] !='X':
            bfs(copied_board2, i, j)
            cnt2 += 1

print(cnt1, cnt2)
                    

        