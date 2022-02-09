import sys
from collections import deque

N, M = map(int, sys.stdin.readline().strip().split())
board = [list(map(int, sys.stdin.readline().strip())) for _ in range(N)]


# 이전에 벽을 뚫었다면 flag는 False
def bfs(board, i, j, flag):
    # 벽 1과 구분하기 위해 음수로 표시
    board[i][j] = -1
    q = deque([(i, j, -1)])
    
    while q:
        i, j, dis = q.popleft()
        
        for dy, dx in [(1,0), (-1,0), (0,1), (0,-1)]:
            if 0<=i+dy<N and 0<=j+dx<M:
                if 
                
                
                
    
bfs(board, 0, 0, True)
print(-board[N-1][M-1])