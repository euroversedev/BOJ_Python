import sys
import copy

N, M = map(int, sys.stdin.readline().strip().split())
board = [list(map(int, sys.stdin.readline().strip().split()))
        for _ in range(N)]

dp = copy.deepcopy(board)
for i in range(N):
    for j in range(N):
        if 0 <= i-1: dp[i][j] += dp[i-1][j]
        if 0 <= j-1: dp[i][j] += dp[i][j-1]
        if 0 <= i-1 and 0 <= j-1 : dp[i][j] -= dp[i-1][j-1]



for _ in range(M):
    x1, y1, x2, y2 = map(int, sys.stdin.readline().strip().split())
    x1, y1, x2, y2 = y1-1, x1-1, y2-1, x2-1
    
    result = dp[y2][x2]
    if 0 <= y1-1: result -= dp[y1-1][x2]
    if 0 <= x1-1: result -= dp[y2][x1-1]
    if 0 <= x1-1 and 0 <= y1-1: result += dp[y1-1][x1-1]
    
    print(result)
    
''' review
계산을 간단히 하려면 제로패딩도 고려해보자.

'''