import sys
sys.setrecursionlimit(10**7)

N, M = map(int, sys.stdin.readline().strip().split())
board = [list(map(int, sys.stdin.readline().strip())) for _ in range(N)]

def dfs(y, x):
    board[y][x] = 2 # 방문처리
    
    if y == N-1:
        print("YES")
        exit()
    
    for dy, dx in [(1,0),(0,1),(-1,0),(0,-1)]:
        if 0<=y+dy<N and 0<=x+dx<M:
            if board[y+dy][x+dx] == 0:
                dfs(y+dy, x+dx)
    
for i in range(M):
    if board[0][i] == 0:
        dfs(0, i)
        
print("NO")