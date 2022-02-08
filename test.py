import sys

T = int(input())
dp = [(0,0) for _ in range(41)]

dp[0] = (1, 0)
dp[1] = (0, 1)
for i in range(2, 41):
    dp[i] = (x + y for x, y in zip(dp[i-1], dp[i-2]))

for _ in range(T):
    N = int(sys.stdin.readline().strip())
    print(dp)