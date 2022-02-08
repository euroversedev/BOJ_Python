import sys

T = int(input())
dp = [(0,0) for _ in range(41)]

dp[0] = (1, 0)
dp[1] = (0, 1)
for i in range(2, 41):
    dp[i] = tuple(dp[i-1][k]+dp[i-2][k] for k in range(2))

for _ in range(T):
    N = int(sys.stdin.readline().strip())
    print(dp[N][0], dp[N][1])