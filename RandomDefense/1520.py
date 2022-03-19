import sys
sys.setrecursionlimit(10**9)

N, M = map(int, sys.stdin.readline().strip().split())
board = [list(map(int, sys.stdin.readline().strip().split()))
        for _ in range(N)]

dp = [[0] * M for _ in range(N)]
# backtracking
def dfs(y, x):
    if y == N-1 and x== M-1:
        return 1
    
    if dp[y][x] != 0:
        return dp[y][x]
    
    for dy, dx in [(1,0),(0,1),(0,-1),(-1,0)]:
        if 0<=y+dy<N and 0<=x+dx<M and board[y][x] > board[y+dy][x+dx]:
            dp[y][x] += dfs(y+dy, x+dx)
    
    return dp[y][x]
    
dfs(0, 0)
print(dp[0][0])