import sys
from collections import deque


d = [-1, 0, 1]

def bfs(board, i, j):
    board[i][j] = 0    # 방문처리
    
    q = deque([(i,j)])
    while q:
        i, j = q.popleft()
        
        for dy in d:
            for dx in d:
                if 0<=i+dy<N and 0<=j+dx<M:
                    if board[i+dy][j+dx] == 1:
                        board[i+dy][j+dx] = 0
                        q.append((i+dy, j+dx))

                    
while True:
    w, h = map(int, sys.stdin.readline().strip().split())
    M, N = w, h
    if (N, M) == (0, 0): break
    
    board = [list(map(int, sys.stdin.readline().strip().split()))
            for _ in range(N)]
    
    cnt = 0
    for i in range(N):
        for j in range(M):
            if board[i][j] == 1:
                bfs(board, i, j)
                cnt += 1
    print(cnt)