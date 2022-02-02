dp = [0, 1, 2, 4] + [0] * 7
for i in range(4, 11):
    dp[i] = dp[i-3] + dp[i-2] + dp[i-1]

N = int(input())
for _ in range(N):
    print(dp[int(input())])


