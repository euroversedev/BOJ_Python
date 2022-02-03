import copy
N = int(input())
array = [list(map(int, input().split())) for _ in range(N)]

dp = copy.deepcopy(array)
for i in range(N-2, -1, -1):
    for j in range(len(dp[i])):
        dp[i][j] += max(dp[i+1][j], dp[i+1][j+1])

print(dp[0][0])