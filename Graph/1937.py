import sys
sys.setrecursionlimit(10**9)

N = int(input())
board = [list(map(int, sys.stdin.readline().strip().split()))
        for _ in range(N)]
dp = [[0] * N for _ in range(N)]

max_ = 0
move = [(1,0),(0,1),(-1,0),(0,-1)]

def dfs(y, x):
    if dp[y][x] > 0:
        return dp[y][x]
    
    dp[y][x] = 1
    for dy, dx in move:
        if 0<=y+dy<N and 0<=x+dx<N:
            if board[y][x] < board[y+dy][x+dx]:
                dp[y][x] = max(dp[y][x], dfs(y+dy, x+dx)+1)
    return dp[y][x]

for i in range(N):
    for j in range(N):
        dfs(i, j)

print(max(map(max, dp)))